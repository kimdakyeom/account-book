import pyshorteners as ps
link = "https://www.youtube.com/shorts/rUXP3nWrPMQ"

sh = ps.Shortener()
short_url = (sh.tinyurl.short(link))

print(short_url)