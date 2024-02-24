from imgui_bundle import imgui, imgui_color_text_edit as ed, imgui_md, ImVec2, ImVec4
from imgui_bundle.immapp import static
import os

TextEditor = ed.TextEditor

def _prepare_text_editor():
    with open(__file__, encoding="utf8") as f:
        this_file_code = f.read()
    editor = TextEditor()
    editor.set_text("""
#==================================================================
#Welcome to imCode
#This is a WIP editor based on Python for Python Competitive Coding
#==================================================================

a = 2
b = 3
print(a+b)
""")
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
        
        if imgui.button("Delete.."):
            imgui.open_popup("Delete?")
        

        # Always center this window when appearing
        center = imgui.get_main_viewport().get_center()
        imgui.set_next_window_pos(center, imgui.Cond_.appearing.value, ImVec2(0.5, 0.5))

        if not hasattr(static, "dont_ask_me_next_time"):
            static.dont_ask_me_next_time = False  # Equivalent to static bool dont_ask_me_next_time = false;

        if imgui.begin_popup_modal("Delete?", None, imgui.WindowFlags_.always_auto_resize.value)[0]:
            imgui.text("All those beautiful files will be deleted.\nThis operation cannot be undone!")
            imgui.separator()

            imgui.push_style_var(imgui.StyleVar_.frame_padding.value, ImVec2(0, 0))
            _, static.dont_ask_me_next_time = imgui.checkbox("Don't ask me next time", static.dont_ask_me_next_time)
            imgui.pop_style_var()

            if imgui.button("OK", ImVec2(120, 0)):
                imgui.close_current_popup()
            imgui.set_item_default_focus()
            imgui.same_line()
            if imgui.button("Cancel", ImVec2(120, 0)):
                imgui.close_current_popup()
            imgui.end_popup()
        imgui.end_main_menu_bar()

    # Text editor
    editor.render("Code")
    imgui.pop_font()

def main():
    from imgui_bundle import immapp
    immapp.run(demo_gui, with_markdown=True)

if __name__ == "__main__":
    main()