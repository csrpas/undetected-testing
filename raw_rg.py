from seleniumbase import SB

with SB(uc=True, test=True, locale_code="en", xvfb=True) as sb:
    url = "https://sistema.rgae.gob.gt/consulta-proveedores"
    sb.activate_cdp_mode(url)
    sb.maximize_window()
    #sb.set_window_size(1366, 768)
    #sb.cdp.gui_click_element("div#MasterGC_ContentBlockHolder_divCaptcha")
    sb.uc_gui_click_captcha()
    #sb.uc_gui_handle_captcha()
    #sb.uc_gui_handle_cf()
    #sb.cdp.gui_click_element("div#MasterGC_ContentBlockHolder_divCaptcha")
    #sb.cdp.uc_gui_click_x_y(1577, 1382)
    sb.sleep(7)
    text = sb.get_text('//label[contains(@class, "required")]')
    print(text)
