"""Define the menu contents, hotkeys, and event bindings.

There is additional configuration information in the EditorWindow class (and
subclasses): the menus are created there based on the menu_specs (class)
variable, and menus not created are silently skipped in the code here.  This
makes it possible, for example, to define a Debug menu which is only present in
the PythonShell window, and a Format menu which is only present in the Editor
windows.

"""
from importlib.util import find_spec

from idlelib.config import idleConf

#   Warning: menudefs is altered in macosx.overrideRootMenu()
#   after it is determined that an OS X Aqua Tk is in use,
#   which cannot be done until after Tk() is first called.
#   Do not alter the 'file', 'options', or 'help' cascades here
#   without altering overrideRootMenu() as well.
#       TODO: Make this more robust

menudefs = [
 # underscore prefixes character to underscore
 ('file', [
   ('_New File', '<<open-new-window>>'),
   ('_Open...', '<<open-window-from-file>>'),
   ('Open _Module...', '<<open-module>>'),
   ('Class _Browser', '<<open-class-browser>>'),
   ('_Path Browser', '<<open-path-browser>>'),
   None,
   ('_Save', '<<save-window>>'),
   ('Save _As...', '<<save-window-as-file>>'),
   ('Save Cop_y As...', '<<save-copy-of-window-as-file>>'),
   None,
   ('Prin_t Window', '<<print-window>>'),
   None,
   ('_Close', '<<close-window>>'),
   ('E_xit', '<<close-all-windows>>'),
  ]),
 ('edit', [
   ('_Undo', '<<undo>>'),
   ('_Redo', '<<redo>>'),
   None,
   ('Cu_t', '<<cut>>'),
   ('_Copy', '<<copy>>'),
   ('_Paste', '<<paste>>'),
   ('Select _All', '<<select-all>>'),
   None,
   ('_Find...', '<<find>>'),
   ('Find A_gain', '<<find-again>>'),
   ('Find _Selection', '<<find-selection>>'),
   ('Find in Files...', '<<find-in-files>>'),
   ('R_eplace...', '<<replace>>'),
   ('Go to _Line', '<<goto-line>>'),
   ('S_how Completions', '<<force-open-completions>>'),
   ('E_xpand Word', '<<expand-word>>'),
   ('Show C_all Tip', '<<force-open-calltip>>'),
   ('Show Surrounding P_arens', '<<flash-paren>>'),

  ]),
('format', [
   ('_Indent Region', '<<indent-region>>'),
   ('_Dedent Region', '<<dedent-region>>'),
   ('Comment _Out Region', '<<comment-region>>'),
   ('U_ncomment Region', '<<uncomment-region>>'),
   ('Tabify Region', '<<tabify-region>>'),
   ('Untabify Region', '<<untabify-region>>'),
   ('Toggle Tabs', '<<toggle-tabs>>'),
   ('New Indent Width', '<<change-indentwidth>>'),
   ('F_ormat Paragraph', '<<format-paragraph>>'),
   ('S_trip Trailing Whitespace', '<<do-rstrip>>'),
   ]),
 ('run', [
   ('Python Shell', '<<open-python-shell>>'),
   ('C_heck Module', '<<check-module>>'),
   ('R_un Module', '<<run-module>>'),
   ]),
 ('shell', [
   ('_View Last Restart', '<<view-restart>>'),
   ('_Restart Shell', '<<restart-shell>>'),
   None,
   ('_Interrupt Execution', '<<interrupt-execution>>'),
   ]),
 ('debug', [
   ('_Go to File/Line', '<<goto-file-line>>'),
   ('!_Debugger', '<<toggle-debugger>>'),
   ('_Stack Viewer', '<<open-stack-viewer>>'),
   ('!_Auto-open Stack Viewer', '<<toggle-jit-stack-viewer>>'),
   ]),
 ('options', [
   ('Configure _IDLE', '<<open-config-dialog>>'),
   ('_Code Context', '<<toggle-code-context>>'),
   ]),
 ('windows', [
   ('Zoom Height', '<<zoom-height>>'),
   ]),
 ('help', [
   ('_About IDLE', '<<about-idle>>'),
   None,
   ('_IDLE Help', '<<help>>'),
   ('Python _Docs', '<<python-docs>>'),
   ]),
]

if find_spec('turtledemo'):
    menudefs[-1][1].append(('Turtle Demo', '<<open-turtle-demos>>'))

default_keydefs = idleConf.GetCurrentKeySet()
