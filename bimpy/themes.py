import bimpy


def __lerp(a, b, t):
    return a + (b - a) * t


def set_light_theme():
    """ light style from Pacome Danhiez (user itamago) https://github.com/ocornut/imgui/pull/511#issuecomment-175719267 """

    style = bimpy.get_style()
    style.set_color(bimpy.Colors.Text, bimpy.Vec4(0.00, 0.00, 0.00, 1.00))
    style.set_color(bimpy.Colors.TextDisabled, bimpy.Vec4(0.60, 0.60, 0.60, 1.00))
    style.set_color(bimpy.Colors.WindowBg, bimpy.Vec4(0.94, 0.94, 0.94, 1.00))
    style.set_color(bimpy.Colors.ChildBg, bimpy.Vec4(0.00, 0.00, 0.00, 0.00))
    style.set_color(bimpy.Colors.PopupBg, bimpy.Vec4(1.00, 1.00, 1.00, 0.98))
    style.set_color(bimpy.Colors.Border, bimpy.Vec4(0.00, 0.00, 0.00, 0.39))
    style.set_color(bimpy.Colors.BorderShadow, bimpy.Vec4(1.00, 1.00, 1.00, 0.10))
    style.set_color(bimpy.Colors.FrameBg, bimpy.Vec4(1.00, 1.00, 1.00, 1.00))
    style.set_color(bimpy.Colors.FrameBgHovered, bimpy.Vec4(0.26, 0.59, 0.98, 0.40))
    style.set_color(bimpy.Colors.FrameBgActive, bimpy.Vec4(0.26, 0.59, 0.98, 0.67))
    style.set_color(bimpy.Colors.TitleBg, bimpy.Vec4(0.96, 0.96, 0.96, 1.00))
    style.set_color(bimpy.Colors.TitleBgCollapsed, bimpy.Vec4(1.00, 1.00, 1.00, 0.51))
    style.set_color(bimpy.Colors.TitleBgActive, bimpy.Vec4(0.82, 0.82, 0.82, 1.00))
    style.set_color(bimpy.Colors.MenuBarBg, bimpy.Vec4(0.86, 0.86, 0.86, 1.00))
    style.set_color(bimpy.Colors.ScrollbarBg, bimpy.Vec4(0.98, 0.98, 0.98, 0.53))
    style.set_color(bimpy.Colors.ScrollbarGrab, bimpy.Vec4(0.69, 0.69, 0.69, 0.80))
    style.set_color(bimpy.Colors.ScrollbarGrabHovered, bimpy.Vec4(0.49, 0.49, 0.49, 0.80))
    style.set_color(bimpy.Colors.ScrollbarGrabActive, bimpy.Vec4(0.49, 0.49, 0.49, 1.00))
    style.set_color(bimpy.Colors.CheckMark, bimpy.Vec4(0.26, 0.59, 0.98, 1.00))
    style.set_color(bimpy.Colors.SliderGrab, bimpy.Vec4(0.26, 0.59, 0.98, 0.78))
    style.set_color(bimpy.Colors.SliderGrabActive, bimpy.Vec4(0.26, 0.59, 0.98, 1.00))
    style.set_color(bimpy.Colors.Button, bimpy.Vec4(0.26, 0.59, 0.98, 0.40))
    style.set_color(bimpy.Colors.ButtonHovered, bimpy.Vec4(0.26, 0.59, 0.98, 1.00))
    style.set_color(bimpy.Colors.ButtonActive, bimpy.Vec4(0.06, 0.53, 0.98, 1.00))
    style.set_color(bimpy.Colors.Header, bimpy.Vec4(0.26, 0.59, 0.98, 0.31))
    style.set_color(bimpy.Colors.HeaderHovered, bimpy.Vec4(0.26, 0.59, 0.98, 0.80))
    style.set_color(bimpy.Colors.HeaderActive, bimpy.Vec4(0.26, 0.59, 0.98, 1.00))
    style.set_color(bimpy.Colors.Separator, bimpy.Vec4(0.39, 0.39, 0.39, 1.00))
    style.set_color(bimpy.Colors.SeparatorHovered, bimpy.Vec4(0.26, 0.59, 0.98, 0.78))
    style.set_color(bimpy.Colors.SeparatorActive, bimpy.Vec4(0.26, 0.59, 0.98, 1.00))
    style.set_color(bimpy.Colors.ResizeGrip, bimpy.Vec4(0.50, 0.50, 0.50, 1.00))
    style.set_color(bimpy.Colors.ResizeGripHovered, bimpy.Vec4(0.26, 0.59, 0.98, 0.67))
    style.set_color(bimpy.Colors.ResizeGripActive, bimpy.Vec4(0.26, 0.59, 0.98, 0.95))
    style.set_color(bimpy.Colors.Tab, __lerp(style.get_color(bimpy.Colors.Header), style.get_color(bimpy.Colors.TitleBgActive), 0.90))
    style.set_color(bimpy.Colors.TabHovered, style.get_color(bimpy.Colors.HeaderHovered))
    style.set_color(bimpy.Colors.TabActive, __lerp(style.get_color(bimpy.Colors.HeaderActive), style.get_color(bimpy.Colors.TitleBgActive), 0.60))
    style.set_color(bimpy.Colors.TabUnfocused, __lerp(style.get_color(bimpy.Colors.Tab), style.get_color(bimpy.Colors.TitleBg), 0.80))
    style.set_color(bimpy.Colors.TabUnfocusedActive, __lerp(style.get_color(bimpy.Colors.TabActive), style.get_color(bimpy.Colors.TitleBg), 0.40))
    style.set_color(bimpy.Colors.PlotLines, bimpy.Vec4(0.39, 0.39, 0.39, 1.00))
    style.set_color(bimpy.Colors.PlotLinesHovered, bimpy.Vec4(1.00, 0.43, 0.35, 1.00))
    style.set_color(bimpy.Colors.PlotHistogram, bimpy.Vec4(0.90, 0.70, 0.00, 1.00))
    style.set_color(bimpy.Colors.PlotHistogramHovered, bimpy.Vec4(1.00, 0.60, 0.00, 1.00))
    style.set_color(bimpy.Colors.TextSelectedBg, bimpy.Vec4(0.26, 0.59, 0.98, 0.35))
    style.set_color(bimpy.Colors.DragDropTarget, bimpy.Vec4(0.26, 0.59, 0.98, 0.95))
    style.set_color(bimpy.Colors.NavHighlight, style.get_color(bimpy.Colors.HeaderHovered))
    style.set_color(bimpy.Colors.NavWindowingHighlight, bimpy.Vec4(0.70, 0.70, 0.70, 0.70))
    style.set_color(bimpy.Colors.NavWindowingDimBg, bimpy.Vec4(0.20, 0.20, 0.20, 0.20))
    style.set_color(bimpy.Colors.ModalWindowDimBg, bimpy.Vec4(0.20, 0.20, 0.20, 0.35))
    bimpy.set_style(style)
