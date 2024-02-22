import ssl
class Configuration(object):
    ssl._create_default_https_context = ssl._create_unverified_context
    encode = "utf-8"
    host = "https://www.eiken.or.jp"
    base_url = host + "/eiken/exam/"
    grades = ["grade_1","grade_p1","grade_2","grade_p2","grade_3","grade_4","grade_5"]
    tag = "div.mt16 a"
    mp3_tag = "div.lyt-audio-01 li.external a"