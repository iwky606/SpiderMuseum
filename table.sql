-- 知识图谱数据库
create
    database museum_knowledge_graph;

use museum_knowledge_graph;


create table museum_items_of_china_v2
(
    id            int primary key auto_increment,
    museum        varchar(255),
    title         varchar(255) comment '标题',
    era           varchar(255) comment '时代',
    material      varchar(255) comment '材质',
    size          varchar(255) comment '尺寸',
    description   text comment '介绍',
    detail_url    varchar(255) comment '详情页面的URL',
    image         varchar(255) comment '文物图片',
    download_link varchar(255) comment '原图下载链接',
    geo           varchar(255) comment '地理位置',
    index (museum),
    index (title),
    index (era)
);

# select count(*)
# from museum_items_of_china_v2
# where museum = 'njmuseum';

# grant select,update,insert,alter on museum_knowledge_graph.museum_items_of_china_v2 to 'museum_knowledge_graph'@'%';
select count(*)/16 from museum_items_of_china_v2 where museum='National Museum of Scotland';

show tables;

select current_user();

show variables like 'general_log%';

set global general_log = 'ON';

SET global log_output = 'table';

select * from mysql.general_log order by event_time desc ;

INSERT INTO museum_items_of_china_v2
        (museum, title, era, material, size, description, detail_url, image, download_link, geo)
        VALUES ('National Museum of Scotland', '计数器', NULL, NULL, NULL, '珍珠母柜台，椭圆形和雕刻，一对之一：中国', 'https://www.nms.ac.uk/explore-our-collections/collection-search-results/counter/315340', 'https://www.nms.ac.uk/images/no_image.gif', 'https://www.nms.ac.uk/images/no_image.gif', '中国'),
               ('National Museum of Scotland', '计数器', NULL, NULL, NULL, '珍珠母柜台，椭圆形和雕刻，一对之一：中国', 'https://www.nms.ac.uk/explore-our-collections/collection-search-results/counter/315341', 'https://www.nms.ac.uk/images/no_image.gif', 'https://www.nms.ac.uk/images/no_image.gif', '中国'),
               ('National Museum of Scotland', '书', '纳西', NULL, NULL, '书用纳西象形文字写，十四张纸缝在\n               左侧，使用纳西族象形符号系统，称为东巴：中国，\n               云南西北部纳西族（藏族），19世纪末至20世纪初', 'https://www.nms.ac.uk/explore-our-collections/collection-search-results/book/315342', 'https://www.nms.ac.uk/images/no_image.gif', 'https://www.nms.ac.uk/images/no_image.gif', '中国'),('National Museum of Scotland', '挂锁', NULL, NULL, NULL, '黄铜挂锁，平行杠型：中国', 'https://www.nms.ac.uk/explore-our-collections/collection-search-results/padlock/315343', 'https://www.nms.ac.uk/images/no_image.gif', 'https://www.nms.ac.uk/images/no_image.gif', '中国'),('National Museum of Scotland', '挂锁钥匙', NULL, NULL, NULL, '黄铜钥匙，用于挂锁：中国', 'https://www.nms.ac.uk/explore-our-collections/collection-search-results/padlock-key/315344', 'https://www.nms.ac.uk/images/no_image.gif', 'https://www.nms.ac.uk/images/no_image.gif', '中国'),('National Museum of Scotland', '印刷版', NULL, NULL, NULL, '木板，长方形，上角倾斜，字符在\n               医院订阅收据的救济：中国', 'https://www.nms.ac.uk/explore-our-collections/collection-search-results/printing-block/315345', 'https://www.nms.ac.uk/images/no_image.gif', 'https://www.nms.ac.uk/images/no_image.gif', '中国'),('National Museum of Scotland', '打印', NULL, NULL, NULL, '打印在红纸上的收据，用于订阅医院：中国', 'https://www.nms.ac.uk/explore-our-collections/collection-search-results/print/315346', 'https://www.nms.ac.uk/images/no_image.gif', 'https://www.nms.ac.uk/images/no_image.gif', '中国'),('National Museum of Scotland', '吸鸦片的灯', NULL, '白色金属', NULL, '阿片类吸烟者用白色金属制成的灯，圆形圆顶形，带有绿色灯芯：\n               中国，公元1859 - 1919年', 'https://www.nms.ac.uk/explore-our-collections/collection-search-results/lamp-opium-smokers/315347', 'https://www.nms.ac.uk/images/no_image.gif', 'https://www.nms.ac.uk/images/no_image.gif', '中国'),('National Museum of Scotland', '灯，吸鸦片者/支架', NULL, '白色金属', NULL, '白色金属制成的吸鸦片灯支架：中国，1859 - 1919年', 'https://www.nms.ac.uk/explore-our-collections/collection-search-results/lamp-opium-smokers-stand/315348', 'https://www.nms.ac.uk/images/no_image.gif', 'https://www.nms.ac.uk/images/no_image.gif', '中国'),('National Museum of Scotland', '灯，吸鸦片的/地球仪', NULL, NULL, NULL, '吸鸦片灯的圆顶玻璃地球仪：中国，1859 - 1919年', 'https://www.nms.ac.uk/explore-our-collections/collection-search-results/lamp-opium-smokers-globe/315349', 'https://www.nms.ac.uk/images/no_image.gif', 'https://www.nms.ac.uk/images/no_image.gif', '中国'),('National Museum of Scotland', '灯，吸鸦片的/戒指', NULL, '白色金属', NULL, '白色金属镂空戒指，用于吸食鸦片的灯：中国，1859 - 1919年', 'https://www.nms.ac.uk/explore-our-collections/collection-search-results/lamp-opium-smokers-ring/315350', 'https://www.nms.ac.uk/images/no_image.gif', 'https://www.nms.ac.uk/images/no_image.gif', '中国'),('National Museum of Scotland', '灯，鸦片吸烟者/笼子', NULL, '白色金属', NULL, '白色金属铁丝笼，带有链条和挂钩，用于悬挂，适合吸食鸦片的人\n               灯：中国，公元1859 - 1919年', 'https://www.nms.ac.uk/explore-our-collections/collection-search-results/lamp-opium-smokers-cage/315351', 'https://www.nms.ac.uk/images/no_image.gif', 'https://www.nms.ac.uk/images/no_image.gif', '中国'),('National Museum of Scotland', '灯，鸦片吸烟者/光盘', NULL, NULL, NULL, '吸鸦片灯的穿孔骨盘：中国，1859 - 1919年', 'https://www.nms.ac.uk/explore-our-collections/collection-search-results/lamp-opium-smokers-disc/315352', 'https://www.nms.ac.uk/images/no_image.gif', 'https://www.nms.ac.uk/images/no_image.gif', '中国'),('National Museum of Scotland', '袖珍秤', NULL, ', ', NULL, '袖珍秤，上面有一根标有圆点的骨头梁、一个平底锅和一个黄铜重物：\n               中国', 'https://www.nms.ac.uk/explore-our-collections/collection-search-results/pocket-steelyard/315353', 'https://www.nms.ac.uk/images/no_image.gif', 'https://www.nms.ac.uk/images/no_image.gif', '中国'),('National Museum of Scotland', '情况', NULL, NULL, NULL, '用竹子做袖珍秤：中国', 'https://www.nms.ac.uk/explore-our-collections/collection-search-results/case/315354', 'https://www.nms.ac.uk/images/no_image.gif', 'https://www.nms.ac.uk/images/no_image.gif', '中国'),('National Museum of Scotland', '茶砖', '清朝，中国（满语）', '压缩茶叶;上表面浮雕，有工人的场景\n               执行各种任务', NULL, '压缩茶叶的长方形砖，带有工人参与的模制场景\n               其上表面的各种任务：中国、清朝、公元19世纪末', 'https://www.nms.ac.uk/explore-our-collections/collection-search-results/tea-brick/315355', 'https://www.nms.ac.uk/search.axd?command=getcontent&server=Detail&width=310&height=285&scalemode=fill&imageformat=png&canvascolor=transparent&value=PF31860', 'https://www.nms.ac.uk/search.axd?command=getcontent&server=Detail&width=310&height=285&scalemode=fill&imageformat=png&canvascolor=transparent&value=PF31860', '中国')