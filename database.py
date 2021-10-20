"""This is a temporary database, in the future I want to do it using SQL"""


def take_link(curse):
    """Класс для работ по курсу"""

    if curse == 'dollar':
        # Доллар
        return 'https://www.google.com/search?sxsrf=ALeKk01NWm6viYijAo3HXYOEQUyDEDtFEw%3A1584716087546&source=hp&ei' \
                     '=N9l0XtDXHs716QTcuaXoAg&q=%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80+%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8' \
                     'E&oq=%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80+&gs_l=psy-ab.3.0.35i39i70i258j0i131l4j0j0i131l4.3044.4178' \
                     '..5294...1.0..0.83.544.7......0....1..gws-wiz.......35i39.5QL6Ev1Kfk4'

    elif curse == 'euro':
        # Евро
        return 'https://www.google.com/search?q=%D0%BA%D1%83%D1%80%D1%81+%D0%B5%D0%B2%D1%80%D0%BE&sxsrf=AOaemvLc9wYK9' \
                   'YrHk5_951xFa52ILPTNkw%3A1633593073190&ei=8aZeYZj_CrHMrgSW9ZOoBA&oq=%D0%BA%D1%83%D1%80%D1%81+%D0%B5%D0' \
                   '%B2%D1%80%D0%BE&gs_lcp=Cgdnd3Mtd2l6EAMYAzIECCMQJzIECCMQJzIECCMQJzIICAAQgAQQsQMyCwgAEIAEELEDEIMBMgsIAB' \
                   'CABBCxAxCDATILCAAQgAQQsQMQgwEyBQgAEIAEMgUIABCABDILCAAQgAQQsQMQgwE6BwgjEOoCECc6DgguEIAEELEDEMcBENEDOgU' \
                   'ILhCABDoICAAQsQMQgwE6CAguEIAEELEDSgUIPBIBM0oECEEYAFDzQ1jvVmDicGgFcAJ4AIABc4gBtASSAQM1LjKYAQCgAQGwAQrA' \
                   'AQE&sclient=gws-wiz'

    if curse == 'CNY':
        # Юань
        return 'https://www.google.com/search?q=%D1%8E%D0%B0%D0%BD%D1%8C+%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E&rlz=1C1' \
                  'CHBD_ruRU893RU893&oq=%D1%8E%D0%B0%D0%BD%D1%8C&aqs=chrome.1.69i57j0i67i433j0i67i131i433j0i67l3j0i512j46' \
                  'i512j0i512l2.2165j0j15&sourceid=chrome&ie=UTF-8'

    if curse == 'DIR':
        # Дирхам
        return 'https://www.google.com/search?q=%D0%BA%D1%83%D1%80%D1%81+%D0%B4%D0%B8%D1%80%D1%85%D0%B0%D0%BC%D0%B0' \
                  '+%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E&rlz=1C1CHBD_ruRU893RU893&oq=%D0%BA%D1%83%D1%80%D1%81+%D0%B4%D0' \
                  '%B8%D1%80&aqs=chrome.0.0i512l4j69i57j0i512j0i10i512j0i512j0i10i512j0i512.3583j1j15&sourceid=chrome&ie' \
                  '=UTF-8 '

    if curse == 'DRA':
        # Драм
        return 'https://www.google.com/search?q=%D0%BA%D1%83%D1%80%D1%81+%D0%B4%D1%80%D0%B0%D0%BC+%D0%BA+%D1%80%D1%83' \
                  '%D0%B1%D0%BB%D1%8E&rlz=1C1CHBD_ruRU893RU893&sxsrf=AOaemvIqGqOHoOjnekOMOdoxahijMfKt1g%3A1633949152235' \
                  '&ei=4BVkYbDgDau1qtsPu42i6A4&oq=%D0%BA%D1%83%D1%80%D1%81+%D0%B4%D1%80%D0%B0%D0%BC+%D0%BA+%D1%80%D1%83' \
                  '%D0%B1%D0%BB%D1%8E&gs_lcp' \
                  '=Cgdnd3Mtd2l6EAEYADIECAAQDTIECAAQDTIECAAQDTIECAAQDTIICAAQCBANEB4yCAgAEAgQDRAeMggIABAIEA0QHjIICAAQCBA' \
                  'NEB46BwgAEEcQsAM6BwgAELADEEM6EAguEMcBEKMCEMgDELADEEM6EAguEMcBENEDEMgDELADEEM6CAgAEAcQChAeOgYIABAHEB5' \
                  'KBQg4EgExSgQIQRgAULXjBFjR7wRgkfsEaAFwAngAgAFSiAHsApIBATWYAQCgAQHIAQvAAQE&sclient=gws-wiz'

    if curse == 'LIR':
        # Лира
        return 'https://www.google.com/search?q=%D0%BA%D1%83%D1%80%D1%81+%D0%BB%D0%B8%D1%80%D0%B0+%D0%BA+%D1%80%return D1%8' \
                '3%D0%B1%D0%BB%D1%8E&rlz=1C1CHBD_ruRU893RU893&sxsrf=AOaemvIbIWGajmtXs7g-cDHyq9Igyf6R-w%3A1633949235285' \
                  '&ei=MxZkYbiAEZCdrgTwgZXgDg&oq=%D0%BA%D1%83%D1%80%D1%81+%D0%BB%D0%B8%D1%80%D0%B0+%D0%BA+%D1%80%D1%83%' \
                  'D0%B1%D0%BB%D1%8E&gs_lcp=Cgdnd3Mtd2l6EAEYADIECAAQDTIECAAQDTIECAAQDTIGCAAQDRAeMgYIABANEB4yBggAEA0QHjII' \
                  'CAAQDRAFEB4yCAgAEA0QBRAeMggIABAIEA0QHjIICAAQCBANEB46BwgAEEcQsAM6BwgAELADEEM6BggAEAcQHkoECEEYAFCulw1Y' \
                  'rp4NYOypDWgBcAJ4AIABY4gB9QOSAQE2mAEAoAEByAEKwAEB&sclient=gws-wiz'

    if curse == 'PES':
        # Песо
        return 'https://www.google.com/search?q=%D0%BA%D1%83%D1%80%D1%81+%D0%BF%D0%B5%D1%81%D0%BE+%D0%BA+%D1%80%return D1%8' \
                '3%D0%B1%D0%BB%D1%8E&rlz=1C1CHBD_ruRU893RU893&sxsrf=AOaemvIbfojRwOKFI-7PQR_SMhMLCWr89w%3A163394945440' \
                  '6&ei=DhdkYaqRGOzErgSLgo-oAg&ved=0ahUKEwiq0L2GmMLzAhVsoosKHQvBAyUQ4dUDCA4&uact=5&oq=%D0%BA%D1%83%D1%8' \
                  '0%D1%81+%D0%BF%D0%B5%D1%81%D0%BE+%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E&gs_lcp=Cgdnd3Mtd2l6EAMyBQgAEI' \
                  'AEMgUIABCABDIGCAAQBxAeMgYIABAHEB4yBggAEAcQHjIGCAAQBxAeMgYIABAHEB4yBggAEAgQHjIGCAAQCBAeMgYIABAIEB46Bwg' \
                  'AEEcQsAM6BwgAELADEEM6BAgAEA06CAgAEAgQBxAeSgQIQRgAUOvjCljG5wpg6ekKaAFwAngAgAFPiAGYApIBATSYAQCgAQHIAQrAA' \
                  'QE&sclient=gws-wiz'

    if curse == 'BAT':
        # Бат
        return 'https://www.google.com/search?q=%D0%BA%D1%83%D1%80%D1%81+%D0%B1%D0%B0%D1%82%D1%82+%D0%BA+%D1%80%Dreturn 1%83' \
                '%D0%B1%D0%BB%D1%8E&rlz=1C1CHBD_ruRU893RU893&sxsrf=AOaemvIbsD4EeeQ7aSppE4ZwCXKMJoPhWA%3A1633949632520&' \
                  'ei=wBdkYe6nH-birgSBjozYCw&ved=0ahUKEwjuh7XbmMLzAhVmsYsKHQEHA7sQ4dUDCA4&uact=5&oq=%D0%BA%D1%83%D1%80%D' \
                  '1%81+%D0%B1%D0%B0%D1%82%D1%82+%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E&gs_lcp=Cgdnd3Mtd2l6EAMyCQgAEAoQRh' \
                  'CCAjIECAAQCjIECAAQCjIECAAQCjIECAAQCjIECAAQCjIECAAQCjIECAAQCjIECAAQCjIECAAQCjoHCAAQRxCwAzoHCAAQsAMQQzo' \
                  'GCAAQBxAeOgQIABANOgUIABCABEoECEEYAFCqwwRY08YEYNfIBGgBcAJ4AIABZ4gBuwKSAQMzLjGYAQCgAQHIAQrAAQE&sclient=' \
                  'gws-wiz'
    if curse == 'FST':
        # Фунт стерлингов
        return 'https://www.google.ru/search?q=%D0%BA%D1%83%D1%80%D1%81+%D1%84%D1%83%D0%BD%D1%82+%D1%81%D1%82%D0%B5%D1' \
                  '%80%D0%BB%D0%B8%D0%BD%D0%B3%D0%B0+%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E&newwindow=1&sxsrf=AOaemvJjnoIl' \
                  'AnrpQDRDtyQVYPbwisyavg%3A1633955192204&ei=eC1kYb2FDOKErwTHgoOABQ&oq=%D0%BA%D1%83%D1%80%D1%81+%D1%84%D1' \
                  '%83%D0%BD%D1%82+%D1%81%D1%82%D0%B5%D1%80%D0%BB%D0%B8%D0%BD%D0%B3%D0%B0+%D0%BA+%D1%80%D1%83%D0%B1%D0%BB' \
                  '%D1%8E&gs_lcp=Cgdnd3Mtd2l6EAMYADIJCCMQJxBGEIICMgoIABCABBCHAhAUMggIABCABBCxAzIFCAAQgAQyBQgAEIAEMgUIABCA' \
                  'BDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQ6BwgjEOoCECc6CwgAEIAEELEDEIMBOg4ILhCABBCxAxDHARCjAjoECCMQJzoEC' \
                  'AAQQzoHCAAQsQMQQzoHCAAQyQMQQzoNCAAQgAQQhwIQsQMQFEoECEEYAFDBJljbOGDtPWgBcAJ4AIABaYgB9ASSAQM3LjGYAQCgAQG' \
                  'wAQrAAQE&sclient=gws-wiz'
    if curse == 'SHF':
        # Швецарский франк
        return 'https://www.google.com/search?q=%D0%BA%D1%83%D1%80%D1%81+idtwfhcrbq+ahfyr+%D0%BA+%D1%80%D1%83%D0%B1%D0' \
                  '%BB%D1%8E&rlz=1C1CHBD_ruRU893RU893&sxsrf=AOaemvKW8a95ox1av70KeBF14JqaF5KDwg%3A1633949798312&ei=ZhhkYc2' \
                  '1EpLargSYobfQBg&ved=0ahUKEwjNgLyqmcLzAhUSrYsKHZjQDWoQ4dUDCA4&uact=5&oq=%D0%BA%D1%83%D1%80%D1%81+idtwfh' \
                  'crbq+ahfyr+%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E&gs_lcp=Cgdnd3Mtd2l6EAMyCQgAEA0QRhCCAjIICAAQDRAFEB4yCA' \
                  'gAEAgQDRAeOgcIABBHELADOgYIABAHEB46BAgAEA06BQgAEM0CSgQIQRgAUJDCBVi86wVg1-wFaANwAngAgAGWAYgB1AqSAQQxNC4y' \
                  'mAEAoAEByAEIwAEB&sclient=gws-wiz'
    if curse == 'IRN':
        # Иена
        return 'https://www.google.com/search?q=%D0%BA%D1%83%D1%80%D1%81+%D0%B8%D0%B5%D0%BD+%D0%BA+%D1%80%D1%83%D0return %B1%' \
                'D0%BB%D1%8E&rlz=1C1CHBD_ruRU893RU893&sxsrf=AOaemvJonlm3PLmMMHDdPj3Ts5Dm1uEZDA%3A1633949895013&ei=xxhkY' \
                  'acO7KOuBIqRofAL&oq=%D0%BA%D1%83%D1%80%D1%81+%D0%B8%D0%B5%D0%BD+%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E&g' \
                  's_lcp=Cgdnd3Mtd2l6EAMYADIECAAQDTIECAAQDTIGCAAQDRAeMgYIABANEB4yBggAEA0QHjIICAAQDRAFEB4yCAgAEAgQDRAeMgoI' \
                  'ABAIEA0QChAeOgcIABBHELADOgYIABAHEB46CAgAEAcQChAeSgQIQRgAUNHIBFjiywRg7NoEaABwAngAgAFpiAHxAZIBAzIuMZgBAK' \
                  'ABAcgBCMABAQ&sclient=gws-wiz'
    if curse == 'AVD':
        # Авст доллар
        return 'https://www.google.com/search?q=%D0%BA%D1%83%D1%80%D1%81+%D0%B0%D0%B2%D1%81%D1%82%D1%80%D0%B0%D0%BB%D0' \
                  '%B8%D0%B9%D1%81%D0%BA%D0%BE%D0%B3%D0%BE+%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80%D0%B0+%D0%BA+%D1%80%D1%83' \
                  '%D0%B1%D0%BB%D1%8E&rlz=1C1CHBD_ruRU893RU893&sxsrf=AOaemvKmncuGJ2TwrTkhFg8CSKOQ0CPFRA%3A1633949973005&e' \
                  'i=FBlkYcvyPOumrgSaxr3wBg&oq=%D0%BA%D1%83%D1%80%D1%81+%D0%B0%D0%B2%D1%81%D1%82%D1%80%D0%B0%D0%BB%D0%B8%' \
                  'D0%B9%D1%81%D0%BA%D0%BE%D0%B3%D0%BE+%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80%D0%B0+%D0%BA+%D1%80%D1%83%D0%' \
                  'B1%D0%BB%D1%8E&gs_lcp=Cgdnd3Mtd2l6EAMYADIGCAAQBxAeMgYIABAHEB4yBggAEAcQHjIGCAAQBxAeMgYIABAHEB4yBggAEAcQ' \
                  'HjIGCAAQBxAeMgYIABAHEB4yBggAEAcQHjIICAAQCBAHEB46BwgAEEcQsAM6BwgAELADEEM6BAgAEA1KBAhBGABQgYEFWNOHBWCYjg' \
                  'VoBHACeACAAU2IAZYCkgEBNJgBAKABAcgBCsABAQ&sclient=gws-wiz'
    if curse == 'GOD':
        # Гонконский доллар
        return 'https://www.google.com/search?q=%D0%BA%D1%83%D1%80%D1%81+%D0%B3%D0%BE%D0%BD%D0%BA%D0%BE%D0%BD%D0%B3+%D' \
                  '0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80%D0%B0+%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E&rlz=1C1CHBD_ruRU893RU89' \
                  '3&sxsrf=AOaemvKlYA8VkGzLfraDPzRkUoQw4tTdQw%3A1633950057399&ei=aRlkYeTkF62SrgSfx5u4BQ&oq=%D0%BA%D1%83%D' \
                  '1%80%D1%81+%D0%B3%D0%BE%D0%BD%D0%BA%D0%BE%D0%BD%D0%B3+%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80%D0%B0+%D0%B' \
                  'A+%D1%80%D1%83%D0%B1%D0%BB%D1%8E&gs_lcp=Cgdnd3Mtd2l6EAMYATIGCAAQDRAeMggIABAIEA0QHjoHCAAQRxCwAzoHCAAQsA' \
                  'MQQzoECAAQDToGCAAQBxAeOggIABAHEAoQHjoFCAAQzQJKBAhBGABQ7aIDWKy0A2DPwgNoAXACeACAAZEBiAHBA5IBAzQuMZgBAKAB' \
                  'AcgBCsABAQ&sclient=gws-wiz'
    if curse == 'RIN':
        # ринггит
        return 'https://www.google.com/search?q=%D0%BA%D1%83%D1%80%D1%81+%D1%80%D0%B8%D0%BD%D0%B3%D0%B3%D0%B8%D1%82+%D' \
                  '0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E&rlz=1C1CHBD_ruRU893RU893&sxsrf=AOaemvJBwPDYxUk5CDQ7UTJT7XYb0ABXaQ%' \
                  '3A1633950115755&ei=oxlkYfLELef1qwGwq6KQBA&oq=%D0%BA%D1%83%D1%80%D1%81+%D1%80%D0%B8%D0%BD%D0%B3%D0%B3%D' \
                  '0%B8%D1%82+%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E&gs_lcp=Cgdnd3Mtd2l6EAMYADIGCAAQDRAeMggIABAIEA0QHjIICA' \
                  'AQCBANEB4yCAgAEAgQDRAeOgcIABBHELADOgYIABAHEB46CAgAEAcQChAeOgoIABAIEAcQChAeOggIABAIEAcQHjoECAAQDUoECEEY' \
                  'AFD1zQ1YnNsNYIXhDWgDcAJ4AIABkgGIAYgEkgEDNS4xmAEAoAEByAEIwAEB&sclient=gws-wiz'
    if curse == 'GUL':
        # Гульден
        return 'https://www.google.com/search?q=%D0%BA%D1%83%D1%80%D1%81+%D0%B3%D1%83%D0%BB%D1%8C%D0%B4%D0%B5%D0%BD+%D' \
                  '0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E&rlz=1C1CHBD_ruRU893RU893&sxsrf=AOaemvJXTra7KDRL1OYzExbHpmkDsZz0_w%' \
                  '3A1633950341925&ei=hRpkYczkN_SGwPAPq6mu0AU&ved=0ahUKEwiMu9etm8LzAhV0AxAIHauUC1oQ4dUDCA4&uact=5&oq=%D0%' \
                  'BA%D1%83%D1%80%D1%81+%D0%B3%D1%83%D0%BB%D1%8C%D0%B4%D0%B5%D0%BD+%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E&' \
                  'gs_lcp=Cgdnd3Mtd2l6EAMyBggAEAcQHjIICAAQCBAHEB4yBggAEAgQHjoHCAAQRxCwAzoECAAQDUoECEEYAFCJ_QRY8YUFYIOKBWg' \
                  'BcAJ4AIABmgGIAboEkgEDNi4xmAEAoAEByAEIwAEB&sclient=gws-wiz'
    if curse == 'LAR':
        # Лари
        return 'https://www.google.com/search?q=%D0%BA%D1%83%D1%80%D1%81+%D0%BB%D0%B0%D1%80%D0%B8+%D0%BA+%D1%80%D1return %83%' \
                'D0%B1%D0%BB%D1%8E&rlz=1C1CHBD_ruRU893RU893&sxsrf=AOaemvKsJMhX6pkT7saOSVUJkOHT5tV9gw%3A1633950425815&ei' \
                  '=2RpkYa2bMaeMrwS594rAAw&oq=%D0%BA%D1%83%D1%80%D1%81+%D0%BB%D0%B0%D1%80%D0%B8+%D0%BA+%D1%80%D1%83%D0%B1' \
                  '%D0%BB%D1%8E&gs_lcp=Cgdnd3Mtd2l6EAEYADIECAAQDTIECAAQDTIECAAQDTIECAAQDTIECAAQDTIECAAQDTIECAAQDTIECAAQDT' \
                  'IECAAQDTIECAAQDToHCAAQRxCwAzoGCAAQDRAeOggIABANEAUQHjoICAAQCBANEB5KBAhBGABQl_ADWPjyA2Cn-wNoAXACeACAAU-I' \
                  'AaYCkgEBNJgBAKABAcgBBMABAQ&sclient=gws-wiz'
