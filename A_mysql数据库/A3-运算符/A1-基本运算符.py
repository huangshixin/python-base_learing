1、算数运算符

  + - * /  (div除  mod取余)
  
  SELECT 100+10,100-10,100/10,100 mod 10 ；
  
################################################################################################################################  

2、比较运算符

    <
    >
    =
    >=
    <=
    <>不等于
    <=>安全等于：   目的是为了和Null进行比较 【两边都是Null---结果为Null，如果有一个不是Null，那么就是0】
    
    
  select 1=2,1!=2,1='1' ,1='a' ; 
  
  结果 【0，1，1，0】  当结果是1='1'时候；系统会转换为同样的；
  【字符串存在隐式转换，如果转换不成功，---直接变成0】
################################################################################################################################  

3、Null
    有null参与比较 ，结果都为Null
  
  
################################################################################################################################  
4、运算符
IS NULL  判断是否为空
IS NOT NULL 是否不为空

LEAST  最小值      select LEAST(CONDITION),GREATEST() FORM DUAL;
GREATEST  最大值

BETWEEN   AND  在某个范围内 (包含两侧)-----条件下届和条件上界 不能对调  |   salary not between a and b
ISNULL    【while ISNULL(CONDITION)】
IN (set)是否在里面
NOT IN  (set)不在其中


LIKE  模糊查询   like 'a%'---a开头匹配  like '%a'  like "%a%"  %代表不确定个数的字符===不区分大小写
    1、包含含 a 和 e  '%a%e%'   "%e%a%"
    2、包含第三个字符为a  "__a%"
    3、查询第二个字符为_  第三个为a  ；这个时候需要进行【转移字符】  "_\_a%"   转义字符\ 
    
    
    
    
REGEXP  正则表达式  :  expr REGEXP (CONDITION)
RLIKE  正则表达式

（1） '^' 匹配以该字符后面的字符开头的字符串
（2） '$' 匹配以该字符前面的字符结尾的字符串
（3） '.' 匹配任何一个单字符  [表示任意一个不确定的字符]
（4） '[...]' 匹配在方括号内的任何字符 :   [abc]  匹配a 或b或c
（5） '*' 匹配零个或多个在它前面的字符；  'X*' 匹配任何数量的x字符
   
  正则表达式可以如下匹配： "%a.*%"； .*表示的是匹配任意多个字符，这个是“.” 匹配任意一个，*表示可以多个；
  
  select 'sadadaf' regexp '^s' ,'daaacvke' regexp 'e$','daviaiofashd' regexp 'ai.f','adasda' regexp '[das]'  from DUAL;
  
################################################################################################################################  
5、逻辑运算符
and 逻辑与
or  逻辑或
not 逻辑非
xor 异或

################################################################################################################################  
6、 按位 与或非  （需要转0 1进制）
&  
|
!
>>右移
<<左移

################################################################################################################################  
