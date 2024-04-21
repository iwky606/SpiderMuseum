-- 知识图谱数据库
create
database museum_knowledge_graph;

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
    detail_url    varchar(255) comment '详情页面的URL',
    image         varchar(255) comment '文物图片',
    download_link varchar(255) comment '原图下载链接',
    index (museum),
    index (title),
    index (era)
);

select count(*) from museum_items_of_china;
#
# create user 'all_privileges_a'@'%' identified by '123456';
# grant all privileges on museum_knowledge_graph.* to 'all_privileges_a'@'%';
# REVOKE ALL PRIVILEGES ON museum_knowledge_graph.* FROM 'all_privileges'@'%';