# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class anjukeItem(scrapy.Item):
    url = scrapy.Field()
    title = scrapy.Field()  # 标题
    price_total = scrapy.Field()  # 总价
    house_code = scrapy.Field()  # 房屋编码
    listed_time = scrapy.Field()  # 挂牌时间
    neighborhood = scrapy.Field()  # 小区
    location = scrapy.Field()  # 位置
    house_age = scrapy.Field()  # 年代
    house_type = scrapy.Field()  # 类型
    room_type = scrapy.Field()  # 户型
    house_area = scrapy.Field()  # 建筑面积
    house_towards = scrapy.Field()  # 朝向
    house_floor = scrapy.Field()  # 楼层
    decoration = scrapy.Field()  # 装修
    price_averages = scrapy.Field()  # 单价
    description = scrapy.Field()  # 房源描述
    house_support = scrapy.Field()  # 小区配套
    contact = scrapy.Field()  # 联系人
    belong = scrapy.Field()  # 联系人所属
    phone_number = scrapy.Field()  # 联系方式


class GFsundeXQ_anjukeItem(scrapy.Item):
    url = scrapy.Field()
    neighborhood = scrapy.Field()  # 小区名称
    price_averages = scrapy.Field()  # 本月均价
    x = scrapy.Field()
    y = scrapy.Field()
    neigh_type = scrapy.Field()  # 物业类型
    building_type = scrapy.Field()  # 建筑类型
    neigh_area = scrapy.Field()  # 占地面积
    building_area = scrapy.Field()  # 建筑面积
    volumetric_rate = scrapy.Field()  # 容积率
    total_floor = scrapy.Field()
    house_age = scrapy.Field()
