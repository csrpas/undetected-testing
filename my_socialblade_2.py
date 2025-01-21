from seleniumbase import SB

with SB(uc=True, test=True, ad_block=True, pls="none") as sb:
    url = "https://socialblade.com/search/search?query=michaelmintz"
    sb.activate_cdp_mode(url)
    sb.sleep(2)
    sb.uc_gui_click_captcha()
    sb.sleep(1)
    print(
        sb.get_text(
            'h2[style="padding-top: 20px; color:#cc6767; font-size: 1.2em;"]'
        )
    )
    print(sb.get_text('h2[style="font-size: 1.1em; color:#ff4c4c;"]'))
