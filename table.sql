-- 知识图谱数据库
create database museum_knowledge_graph;

use museum_knowledge_graph;

create table museum_items_of_china
(
    id            int primary key auto_increment,
    museum        varchar(255),
    title         varchar(255) comment '标题',
    era           varchar(255) comment '时代',
    material      varchar(255) comment '材质',
    size          varchar(255) comment '尺寸',
    description   text comment '介绍',
    url           varchar(255) comment '详情页面的URL',
    image         varchar(255) comment '文物图片' unique,
    download_link varchar(255) comment '原图下载链接',
    index (museum),
    index (title),
    index (era)
);

