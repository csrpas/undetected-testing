from seleniumbase import SB

with SB(uc=True, test=True, locale_code="en") as sb:
    url = "https://www.guatecompras.gt/proveedores/busquedaProvee.aspx"
    sb.activate_cdp_mode(url)
    sb.press_keys("#MasterGC_ContentBlockHolder_txtNit", "87560100")
    sb.sleep(10)
    sb.uc_click('input#MasterGC_ContentBlockHolder_cmdNit')
    sb.sleep(20)
    sb.uc_gui_click_captcha()
    sb.sleep(10)
    print(sb.get_text("//*[@id='MasterGC_ContentBlockHolder_lblNombreProv']"))
