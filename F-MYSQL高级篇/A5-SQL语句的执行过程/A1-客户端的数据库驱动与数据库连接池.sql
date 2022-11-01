2.1 客户端的数据库驱动与数据库连接池：

  （1） 客户端与数据库进行通信前，通过数据库驱动与MYSQL建立连接，建立完成之后，就发送sql语句；
  
  （2）为了减少频繁创建和销毁连接造成系统性能的下降，通过数据库连接池维护一点数量的执行过程
  ，当需要进行连接时，就直接从连接池中获取，使用完毕之后，再归还给连接池。
  
  
2.2 、MYSQL架构的Server层的执行过程：

  （1） 连接器：主要负责跟客户端建立连接、获取权限、维持和管理连接；
  （2）查询缓存【在mysql8.0，直接删除了】：优先在缓存中进行查询，如果查到了则直接返回，如果缓存中查不到，在数据库中查询；
  
  （3）解析器/分析器：分析器的工作主要是对要执行的SQL语句进行词法解析、语法解析，最终得到语法抽象树，，然后再使用预处理器对抽象语法树进行语义校验；
  判断抽象语法树如果存在的情况，再接着判断select投影字段是否再表中存在；
  
  
  （4）优化器：主要将SQL经过词法解析、语法解析得到的语法树，通过数据字典和统计信息的内容，再经过一系列的运算，最终得出一个执行计划
  
  （5）执行器：根据一系列的执行计划去调用存储引擎提供的API接口去调用操作数据，完成SQL的执行。
  
  
  
2.3 Innodb存储引擎的执行过程：
（1）首先MySQL执行器根据 执行计划 调用存储引擎的API查询数据
（2）存储引擎先从缓存池buffer pool中查询数据，如果没有就会去磁盘中查询，如果查询到了就将其放到缓存池中
（3）在数据加载到 Buffer Pool 的同时，会将这条数据的原始记录保存到 undo 日志文件中
（4）innodb 会在 Buffer Pool 中执行更新操作
（5）更新后的数据会记录在 redo log buffer 中
（6）提交事务在提交的同时会做以下三件事
（7）（第一件事）将redo log buffer中的数据刷入到redo log文件中
（8）（第二件事）将本次操作记录写入到 bin log文件中
（9）（第三件事）将bin log文件名字和更新内容在 bin log 中的位置记录到redo log中，同时在 redo log 最后添加 commit 标记
（10）使用一个后台线程，它会在某个时机将我们Buffer Pool中的更新后的数据刷到 MySQL 数据库中，这样就将内存和数据库的数据保持统一了

