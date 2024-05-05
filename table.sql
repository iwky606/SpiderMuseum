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
select count(*) from museum_items_of_china_v2 where museum='National Museum of Scotland';

show tables;

select current_user();

show variables like 'general_log%';

set global general_log = 'ON';

SET global log_output = 'table';

select * from mysql.general_log order by event_time desc ;
