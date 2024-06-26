-- 知识图谱数据库
create database museum_knowledge_graph;

use museum_knowledge_graph;

create table museum_items_of_china_v3
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

grant create,select,update,insert on museum_knowledge_graph.* to 'museum_knowledge_graph'@'%';
flush privileges ;


select *
from museum_items_of_china_v2
where museum='njmuseum'
limit 1;