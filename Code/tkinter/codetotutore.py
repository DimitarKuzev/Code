# -*- coding: utf-8  -*-
"""
A window with a unicode textfield where the user can edit.

Useful for editing the contents of an article.
"""

#
# (C) Rob W.W. Hooft, 2003
# (C) Daniel Herding, 2004
#     Wikiwichtel
# (C) pywikibot team, 2008-2014
#
# Distributed under the terms of the MIT license.
#
__version__ = '$Id: f141d9bcde47eb5b9454b407921d9e898d3030de $'
#

import sys
if sys.version_info[0] > 2:
    import tkinter as Tkinter
    from tkinter.scrolledtext import ScrolledText
    from tkinter import simpledialog as tkSimpleDialog
else:
    import Tkinter
    from ScrolledText import ScrolledText
    import tkSimpleDialog

from idlelib import SearchDialog, ReplaceDialog, configDialog
from idlelib.configHandler import idleConf
from idlelib.MultiCall import MultiCallCreator


class TextEditor(ScrolledText):
    """A text widget with some editing enhancements.

    A lot of code here is copied or adapted from the idlelib/EditorWindow.py
    file in the standard Python distribution.

    """
    def __init__(self, master=None, **kwargs):
        # get default settings from user's IDLE configuration
        currentTheme = idleConf.CurrentTheme()
        textcf = dict(padx=5, wrap='word', undo='True',
                      foreground=idleConf.GetHighlight(currentTheme,
                                                       'normal', fgBg='fg'),
                      background=idleConf.GetHighlight(currentTheme,
                                                       'normal', fgBg='bg'),
                      highlightcolor=idleConf.GetHighlight(currentTheme,
                                                           'hilite', fgBg='fg'),
                      highlightbackground=idleConf.GetHighlight(currentTheme,
                                                                'hilite',
                                                                fgBg='bg'),
                      insertbackground=idleConf.GetHighlight(currentTheme,
                                                             'cursor',
                                                             fgBg='fg'),
                      width=idleConf.GetOption('main', 'EditorWindow', 'width'),
                      height=idleConf.GetOption('main', 'EditorWindow',
                                                'height')
                      )
        fontWeight = 'normal'
        if idleConf.GetOption('main', 'EditorWindow', 'font-bold', type='bool'):
            fontWeight = 'bold'
        textcf['font'] = (idleConf.GetOption('main', 'EditorWindow', 'font'),
                          idleConf.GetOption('main', 'EditorWindow',
                                             'font-size'),
                          fontWeight)
        # override defaults with any user-specified settings
        textcf.update(kwargs)
        ScrolledText.__init__(self, master, **textcf)

    def add_bindings(self):
        # due to IDLE dependencies, this can't be called from __init__
        # add key and event bindings
        self.bind("<<cut>>", self.cut)
        self.bind("<<copy>>", self.copy)
        self.bind("<<paste>>", self.paste)
        self.bind("<<select-all>>", self.select_all)
        self.bind("<<remove-selection>>", self.remove_selection)
        self.bind("<<find>>", self.find_event)
        self.bind("<<find-again>>", self.find_again_event)
        self.bind("<<find-selection>>", self.find_selection_event)
        self.bind("<<replace>>", self.replace_event)
        self.bind("<<goto-line>>", self.goto_line_event)
        self.bind("<<del-word-left>>", self.del_word_left)
        self.bind("<<del-word-right>>", self.del_word_right)
        keydefs = {'<<copy>>': ['<Control-Key-c>', '<Control-Key-C>'],
                   '<<cut>>': ['<Control-Key-x>', '<Control-Key-X>'],
                   '<<del-word-left>>': ['<Control-Key-BackSpace>'],
                   '<<del-word-right>>': ['<Control-Key-Delete>'],
                   '<<end-of-file>>': ['<Control-Key-d>', '<Control-Key-D>'],
                   '<<find-again>>': ['<Control-Key-g>', '<Key-F3>'],
                   '<<find-selection>>': ['<Control-Key-F3>'],
                   '<<find>>': ['<Control-Key-f>', '<Control-Key-F>'],
                   '<<goto-line>>': ['<Alt-Key-g>', '<Meta-Key-g>'],
                   '<<paste>>': ['<Control-Key-v>', '<Control-Key-V>'],
                   '<<redo>>': ['<Control-Shift-Key-Z>'],
                   '<<remove-selection>>': ['<Key-Escape>'],
                   '<<replace>>': ['<Control-Key-h>', '<Control-Key-H>'],
                   '<<select-all>>': ['<Control-Key-a>'],
                   '<<undo>>': ['<Control-Key-z>', '<Control-Key-Z>'],
                   }

        for event, keylist in keydefs.items():
            if keylist:
                self.event_add(event, *keylist)

    def cut(self, event):
        if self.tag_ranges("sel"):
            self.event_generate("<<Cut>>")
        return "break"

    def copy(self, event):
        if self.tag_ranges("sel"):
            self.event_generate("<<Copy>>")
        return "break"

    def paste(self, event):
        self.event_generate("<<Paste>>")
        return "break"

    def select_all(self, event=None):
        self.tag_add("sel", "1.0", "end-1c")
        self.mark_set("insert", "1.0")
        self.see("insert")
        return "break"

    def remove_selection(self, event=None):
        self.tag_remove("sel", "1.0", "end")
        self.see("insert")

    def del_word_left(self, event):
        self.event_generate('<Meta-Delete>')
        return "break"

    def del_word_right(self, event=None):
        self.event_generate('<Meta-d>')
        return "break"

    def find_event(self, event=None):
        if not self.tag_ranges("sel"):
            found = self.tag_ranges("found")
            if found:
                self.tag_add("sel", found[0], found[1])
            else:
                self.tag_add("sel", "1.0", "1.0+1c")
        SearchDialog.find(self)
        return "break"

    def find_again_event(self, event=None):
        SearchDialog.find_again(self)
        return "break"

    def find_selection_event(self, event=None):
        SearchDialog.find_selection(self)
        return "break"

    def replace_event(self, event=None):
        ReplaceDialog.replace(self)
        return "break"

    def find_all(self, s):
        """
        Highlight all occurrences of string s, and select the first one.

        If the string has already been highlighted, jump to the next occurrence
        after the current selection. (You cannot go backwards using the
        button, but you can manually place the cursor anywhere in the
        document to start searching from that point.)

        """
        if hasattr(self, "_highlight") and self._highlight == s:
            try:
                if self.get(Tkinter.SEL_FIRST, Tkinter.SEL_LAST) == s:
                    return self.find_selection_event(None)
                else:
                    # user must have changed the selection
                    found = self.tag_nextrange('found', Tkinter.SEL_LAST)
            except Tkinter.TclError:
                # user must have unset the selection
                found = self.tag_nextrange('found', Tkinter.INSERT)
            if not found:
                # at last occurrence, scroll back to the top
                found = self.tag_nextrange('found', 1.0)
            if found:
                self.do_highlight(found[0], found[1])
        else:
            # find all occurrences of string s;
            # adapted from O'Reilly's Python in a Nutshell
            # remove previous uses of tag 'found', if any
            self.tag_remove('found', '1.0', Tkinter.END)
            if s:
                self._highlight = s
                # start from the beginning (and when we come to the end, stop)
                idx = '1.0'
                while True:
                    # find next occurence, exit loop if no more
                    idx = self.search(s, idx, nocase=1, stopindex=Tkinter.END)
                    if not idx:
                        break
                    # index right after the end of the occurence
                    lastidx = '%s+%dc' % (idx, len(s))
                    # tag the whole occurence (start included, stop excluded)
                    self.tag_add('found', idx, lastidx)
                    # prepare to search for next occurence
                    idx = lastidx
                # use a red foreground for all the tagged occurences
                self.tag_config('found', foreground='red')
                found = self.tag_nextrange('found', 1.0)
                if found:
                    self.do_highlight(found[0], found[1])

    def do_highlight(self, start, end):
        """Select and show the text from index start to index end."""
        self.see(start)
        self.tag_remove(Tkinter.SEL, '1.0', Tkinter.END)
        self.tag_add(Tkinter.SEL, start, end)
        self.focus_set()

    def goto_line_event(self, event):
        lineno = tkSimpleDialog.askinteger("Goto", "Go to line number:",
                                           parent=self)
        if lineno is None:
            return "break"
        if lineno <= 0:
            self.bell()
            return "break"
        self.mark_set("insert", "%d.0" % lineno)
        self.see("insert")


class EditBoxWindow(Tkinter.Frame):

    def __init__(self, parent=None, **kwargs):
        if parent is None:
            # create a new window
            parent = Tkinter.Tk()
        self.parent = parent
        Tkinter.Frame.__init__(self, parent)
        self.editbox = MultiCallCreator(TextEditor)(self, **kwargs)
        self.editbox.pack(side=Tkinter.TOP)
        self.editbox.add_bindings()
        self.bind("<<open-config-dialog>>", self.config_dialog)

        bottom = Tkinter.Frame(parent)
        # lower left subframe which will contain a textfield and a Search button
        bottom_left_frame = Tkinter.Frame(bottom)
        self.textfield = Tkinter.Entry(bottom_left_frame)
        self.textfield.pack(side=Tkinter.LEFT, fill=Tkinter.X, expand=1)

        buttonSearch = Tkinter.Button(bottom_left_frame, text='Find next',
                                      command=self.find)
        buttonSearch.pack(side=Tkinter.RIGHT)
        bottom_left_frame.pack(side=Tkinter.LEFT, expand=1)

        # lower right subframe which will contain OK and Cancel buttons
        bottom_right_frame = Tkinter.Frame(bottom)

        buttonOK = Tkinter.Button(bottom_right_frame, text='OK',
                                  command=self.pressedOK)
        buttonCancel = Tkinter.Button(bottom_right_frame, text='Cancel',
                                      command=parent.destroy)
        buttonOK.pack(side=Tkinter.LEFT, fill=Tkinter.X)
        buttonCancel.pack(side=Tkinter.RIGHT, fill=Tkinter.X)
        bottom_right_frame.pack(side=Tkinter.RIGHT, expand=1)

        bottom.pack(side=Tkinter.TOP)

        # create a toplevel menu
        menubar = Tkinter.Menu(self.parent)

        findmenu = Tkinter.Menu(menubar)
        findmenu.add_command(label="Find",
                             command=self.editbox.find_event,
                             accelerator="Ctrl+F",
                             underline=0)
        findmenu.add_command(label="Find again",
                             command=self.editbox.find_again_event,
                             accelerator="Ctrl+G",
                             underline=6)
        findmenu.add_command(label="Find all",
                             command=self.find_all,
                             underline=5)
        findmenu.add_command(label="Find selection",
                             command=self.editbox.find_selection_event,
                             accelerator="Ctrl+F3",
                             underline=5)
        findmenu.add_command(label="Replace",
                             command=self.editbox.replace_event,
                             accelerator="Ctrl+H",
                             underline=0)
        menubar.add_cascade(label="Find", menu=findmenu, underline=0)

        editmenu = Tkinter.Menu(menubar)
        editmenu.add_command(label="Cut",
                             command=self.editbox.cut,
                             accelerator="Ctrl+X",
                             underline=2)
        editmenu.add_command(label="Copy",
                             command=self.editbox.copy,
                             accelerator="Ctrl+C",
                             underline=0)
        editmenu.add_command(label="Paste",
                             command=self.editbox.paste,
                             accelerator="Ctrl+V",
                             underline=0)
        editmenu.add_separator()
        editmenu.add_command(label="Select all",
                             command=self.editbox.select_all,
                             accelerator="Ctrl+A",
                             underline=7)
        editmenu.add_command(label="Clear selection",
                             command=self.editbox.remove_selection,
                             accelerator="Esc")
        menubar.add_cascade(label="Edit", menu=editmenu, underline=0)

        optmenu = Tkinter.Menu(menubar)
        optmenu.add_command(label="Settings...",
                            command=self.config_dialog,
                            underline=0)
        menubar.add_cascade(label="Options", menu=optmenu, underline=0)

        # display the menu
        self.parent.config(menu=menubar)
        self.pack()

    def edit(self, text, jumpIndex=None, highlight=None):
        """
        Provide user with editor to modify text.

        Parameters:
            * text      - a Unicode string
            * jumpIndex - an integer: position at which to put the caret
            * highlight - a substring; each occurence will be highlighted
        """
        self.text = None
        # put given text into our textarea
        self.editbox.insert(Tkinter.END, text)
        # wait for user to push a button which will destroy (close) the window
        # enable word wrap
        self.editbox.tag_add('all', '1.0', Tkinter.END)
        self.editbox.tag_config('all', wrap=Tkinter.WORD)
        # start search if required
        if highlight:
            self.find_all(highlight)
        if jumpIndex:
            print(jumpIndex)
            # lines are indexed starting at 1
            line = text[:jumpIndex].count('\n') + 1
            column = jumpIndex - (text[:jumpIndex].rfind('\n') + 1)
            # don't know how to place the caret, but scrolling to the right line
            # should already be helpful.
            self.editbox.see('%d.%d' % (line, column))
        # wait for user to push a button which will destroy (close) the window
        self.parent.mainloop()
        return self.text

    def find_all(self, target):
        self.textfield.insert(Tkinter.END, target)
        self.editbox.find_all(target)

    def find(self):
        # get text to search for
        s = self.textfield.get()
        if s:
            self.editbox.find_all(s)

    def config_dialog(self, event=None):
        configDialog.ConfigDialog(self, 'Settings')

    def pressedOK(self):
        # called when user pushes the OK button.
        # saves the buffer into a variable, and closes the window.
        self.text = self.editbox.get('1.0', Tkinter.END)
        # if the editbox contains ASCII characters only, get() will
        # return string, otherwise unicode (very annoying). We only want
        # it to return unicode, so we work around this.
        if isinstance(self.text, str):
            self.text = unicode(self.text)
        self.parent.destroy()

    def debug(self, event=None):
        self.quit()
        return "break"


# the following class isn't used anywhere in the framework: ####
class ListBoxWindow:

    # called when user pushes the OK button.
    # closes the window.
    def pressedOK(self):
        # ok closes listbox
        self.parent.destroy()

    def __init__(self, parent=None):
        if parent is None:
            # create a new window
            parent = Tkinter.Tk()
        self.parent = parent

        # selectable: only one item
        self.listbox = Tkinter.Listbox(parent, selectmode=Tkinter.SINGLE)
        # put list into main frame, using all available space
        self.listbox.pack(anchor=Tkinter.CENTER, fill=Tkinter.BOTH)

        # lower subframe which will contain one button
        self.bottom_frame = Tkinter.Frame(parent)
        self.bottom_frame.pack(side=Tkinter.BOTTOM)

        buttonOK = Tkinter.Button(self.bottom_frame, text='OK', command=self.pressedOK)
        buttonOK.pack(side=Tkinter.LEFT, fill=Tkinter.X)
        # idea: set title to cur_disambiguation

    def list(self, list):
        # put list of alternatives into listbox
        self.list = list
        # find required area
        laenge = len(list)
        maxbreite = 0
        for i in range(laenge):
            # cycle through all listitems to find maxlength
            if len(list[i]) + len(str(i)) > maxbreite:
                maxbreite = len(list[i]) + len(str(i))
            # show list as formerly in DOS-window
            self.listbox.insert(Tkinter.END, str(i) + ' - ' + list[i])
        # set optimized height & width
        self.listbox.config(height=laenge, width=maxbreite + 2)
        # wait for user to push a button which will destroy (close) the window
        return self.list


if __name__ == "__main__":
    import pywikibot
    try:
        root = Tkinter.Tk()
        root.resizable(width=Tkinter.FALSE, height=Tkinter.FALSE)
        root.title("pywikibot GUI")
        page = pywikibot.Page(pywikibot.Site(), u'Main Page')
        content = page.get()
        myapp = EditBoxWindow(root)
        myapp.bind("<Control-d>", myapp.debug)
        v = myapp.edit(content, highlight=page.title())
    finally:
        pywikibot.stopme()