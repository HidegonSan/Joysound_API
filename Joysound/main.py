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
