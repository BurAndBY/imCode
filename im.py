from imgui_bundle import imgui, imgui_color_text_edit as ed, imgui_md
from imgui_bundle.immapp import static
import os

TextEditor = ed.TextEditor

def _prepare_text_editor():
    with open(__file__, encoding="utf8") as f:
        this_file_code = f.read()
    editor = TextEditor()
    editor.set_text(this_file_code)
    editor.set_language_definition(TextEditor.LanguageDefinition.python())
    editor.set_palette(ed.TextEditor.get_dark_palette())
    return editor

@static(editor=_prepare_text_editor())
def demo_gui():
    static = demo_gui
    editor = static.editor
    imgui.push_font(imgui_md.get_code_font())

    # Top bar with file options
    if imgui.begin_main_menu_bar():
        if imgui.begin_menu("File", True):
            clicked_new, selected_new = imgui.menu_item("New", 'N', False, True)
            clicked_open, selected_open = imgui.menu_item("Open", 'O', False, True)
            clicked_save, selected_save = imgui.menu_item("Save", 'S', False, True)
            if clicked_save:
                # Save the file
                with open(os.path.basename(__file__), 'w', encoding='utf8') as f:
                    f.write(editor.get_text())
            imgui.end_menu()
        if imgui.begin_menu("Tools", True):
            clicked_hash, selected_hash = imgui.menu_item("HashConf", 'H', False, True)
            clicked_find, selected_find = imgui.menu_item("Find", "F", False, True)

            if clicked_hash:
                editor.set_palette(ed.TextEditor.get_dark_palette())
                editor.set_language_definition(TextEditor.LanguageDefinition.python())
                editor.set_show_whitespaces(True)
                           
            imgui.end_menu()
        imgui.end_main_menu_bar()

    # Text editor
    editor.render("Code")
    imgui.pop_font()

def main():
    from imgui_bundle import immapp
    immapp.run(demo_gui, with_markdown=True)

if __name__ == "__main__":
    main()