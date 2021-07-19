import requests
import json


def searchSongs(title):
	url = "https://mspxy.joysound.com/Common/ContentsList"
	params = {"format": "all", "kindCnt": "1", "start": "1", "count": "20",
	"sort": "popular", "order": "desc", "kind1": "song", "word1": title, "match1": "partial",
	"apiVer": "1.0"}
	headers = {'X-JSP-APP-NAME': '0000800', 'Content-Type': 'application/x-www-form-urlencoded'}
	response = requests.post(url, params=params, headers=headers)
	return response.json()


def getLyric(id):
	url = "https://mspxy.joysound.com/Common/Lyric"
	params = {"kind": "naviGroupId", "selSongNo": id, "interactionFlg": "0", "apiVer": "1.0"}
	headers = {'X-JSP-APP-NAME': '0000800', 'Content-Type': 'application/x-www-form-urlencoded'}
	response = requests.post(url, params=params, headers=headers)
	return response.json()


def getTop(title):
	search = searchSongs(title)
	if search["hitCount"] == "0":
		return None
	id = search["contentsList"][0]["naviGroupId"]
	lyric = getLyric(id)
	songName = lyric["songName"]
	ly = lyric["lyricList"][0]["lyric"]
	return (songName, ly)




"""
('浮舟', '春の匂いも\n芽吹く花も\n\n立ちすくむあたしに\n君を連れてはこない\n\n夏が来る頃は\n明け方の雨\n\n静かに寄り添って\nかけら拾い集める\n\n秋が過ぎたら\nきっとあたしは\n\nのびた黒い髪を\n切り落としてしまう\n\n愛しい人よ\n離れ顔なんて\n\n3日もすりゃ\nすぐに忘れてしまった\n\nただ染みついて\n消え ないのは煙草の匂い\n\n君を待つ日々は足りない\n切ない 鳴り止まない\n\n不協和音が 響き合って\nそれがあたしの枯れない\n\n溶けない 鳴り止まない\n孤独の唄\n\n来… 来来 来来 来来来\n来来 来来 来来来 Ah...\n\n来来 来来 来来来\n来来 来来 来来来\n\nかすかな別れを\n漂わすこともなく\n\n足音は突然\n絶切れた あ \n\n悲しくも美しき\n白い冬\n\n会えるものならば\n他に何も望まない\n\n降り積もるは あの日も雪\n君を待つ日々は\n\n足りない 切ない\n鳴り止まない\n\n不協和音が響き合って\nそれがあたしの枯れない\n\n溶けない 鳴り止まない\n孤独の唄\n\n来… 来来 来来 来来来\n来来 来来 来来来 Ah...\n\n来来 来来 来来来\n孤独の  来来来\n')
"""
