from collections import defaultdict
import re

def solution(word, pages):
    default = []
    # 기본점수, 외부 링크 수, 현재 페이지의 링크
    for page in pages:
        score = 0
        for f in re.findall(r'[a-zA-Z]+', page.lower()):
            if f == word.lower():
                score += 1
        default.append(score)
    # default = [page.lower().count(word.lower()) for page in pages]
    ext_link = [page.count('<a') for page in pages]
    cur_link = [page[page.find('content=')+8:page.find('/>')].strip('"') for page in pages]
    cur_link_dic = {}
    for i in range(len(cur_link)):
        cur_link_dic[cur_link[i]] = i

    link_score = []
    links = [[] for _ in range(len(default))]
    for i in range(len(ext_link)):
        idx = 0
        link = []
        for j in range(ext_link[i]):
            idx = pages[i].find('href=', idx+1)
            link.append(pages[i][idx:pages[i].find('">', idx)].strip('href=').strip('"'))
            if link[j] not in cur_link_dic:
                continue
            links[cur_link_dic[link[j]]].append(default[i] / ext_link[i])
        
    links = [sum(x) for x in links]
    res = [a + b for a, b in zip(default, links)]
    # print(default)
    # print(ext_link)
    # print(cur_link)
    # print(link_score, res)

    return res.index(max(res))


  
print(solution('blind', ["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://a.com\"/>\n</head>  \n<body>\nBlind Lorem Blind ipsum dolor Blind test sit amet, consectetur adipiscing elit. \n<a href=\"https://b.com\"> Link to b </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://b.com\"/>\n</head>  \n<body>\nSuspendisse potenti. Vivamus venenatis tellus non turpis bibendum, \n<a href=\"https://a.com\"> Link to a </a>\nblind sed congue urna varius. Suspendisse feugiat nisl ligula, quis malesuada felis hendrerit ut.\n<a href=\"https://c.com\"> Link to c </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://c.com\"/>\n</head>  \n<body>\nUt condimentum urna at felis sodales rutrum. Sed dapibus cursus diam, non interdum nulla tempor nec. Phasellus rutrum enim at orci consectetu blind\n<a href=\"https://a.com\"> Link to a </a>\n</body>\n</html>"]))
print(solution('Muzi', ["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://careers.kakao.com/interview/list\"/>\n</head>  \n<body>\n<a href=\"https://programmers.co.kr/learn/courses/4673\"></a>#!MuziMuzi!)jayg07con&&\n\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://www.kakaocorp.com\"/>\n</head>  \n<body>\ncon%\tmuzI92apeach&2<a href=\"https://hashcode.co.kr/tos\"></a>\n\n\t^\n</body>\n</html>"]))
