from seleniumbase import SB

with SB(uc=True, test=True, locale_code="en") as sb:
    url = "https://gitlab.com/users/sign_in"
    sb.activate_cdp_mode(url)
    sb.uc_gui_click_captcha()
    sb.sleep(2)
    print(sb.get_text("label[for='user_login']"))
