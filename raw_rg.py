from seleniumbase import SB

with SB(uc=True, test=True, locale_code="en", xvfb=True) as sb:
    url = "https://sistema.rgae.gob.gt/consulta-proveedores"
    sb.activate_cdp_mode(url)
    sb.maximize_window()
    sb.uc_gui_click_captcha()
    sb.sleep(7)
    text = sb.get_text('//label[contains(@class, "required")]')
    print(text)
