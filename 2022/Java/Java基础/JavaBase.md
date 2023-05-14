Java介于编译型语言和解释型语言之间。编译型语言如C、C++，代码是直接编译成机器码执行，但是不同的平台（x86、ARM等）CPU的指令集不同，因此，需要编译出每一种平台的对应机器码。解释型语言如Python、Ruby没有这个问题，可以由解释器直接加载源码然后运行，代价是运行效率太低。而Java是将代码编译成一种“字节码”，它类似于抽象的CPU指令，然后，针对不同平台编写虚拟机，不同平台的虚拟机负责加载字节码并执行，这样就实现了“一次编写，到处运行”的效果。




## 1 什么是JDK，JRE
**1. JDK基本介绍**

1) JDK的全称(Java Development Kit————Java 开发工具包)
JDK = JRE + java的开发工具[java, javac,javadoc,javap等]
2) JDK 是提供给Java开发人员使用的，其中包含了java的开发工具，也包括了JRE。所以安装了JDK，就不用在单独安装JRE了。

**2. JRE基本介绍**

1) JRE(Java Runtime Environment————Java运行环境)
JRE = JVM + Java的核心类库[类]

2) 包括Java虚拟机(JVM Java Virtual Machine)和Java程序所需的核心类库等，如果想要运行一个开发好的Java程序，
计算机中只需要安装JRE即可。

**3. JDK、JRE 和JVM 的包含关系**

1) JDK = JRE + 开发工具集（例如Javac, java编译工具等)
2) JRE = JVM + Java SE 标准类库（java核心类库）
3) 如果只想运行开发好的.class文件只需要JRE

**4. 下载、安装JDK**
1）下载安装
根据自己的设备选择对应安装包，[https://www.oracle.com/java/technologies/downloads/](https://www.oracle.com/java/technologies/downloads/)

温馨提示：安装路径不要有中文或者特殊符号如空格等。比如`d:\program\jdk8`。当提示安装JRE时，可以选择不安装,也可以安装.

2）配置环境变量path的步骤
1. 我的电脑--属性--高级系统设置--环境变量
2. 增加JAVA_HOME环境变量，指向jdk的安装目录`d:\program\jdk8`
3. 编辑path环境变量，增加`%JAVA HOME%\bin`
4. 打开DOS命令行，任意目录下敲入javac/java。如果出现javac的参数信息，配置成功。

**5. Java 开发注意事项和细节说明**

1. Java源文件以.java为扩展名。源文件的基本组成部分是类(class)，如本类中的Hello类。
2. Java应用程序的执行入口是main()方法。它有固定的书写格式: `public static void main(String[] args){...}`
3. Java语言严格区分大小写。
4. Java方法由一条条语句构成，每个语句以“”结束。
5. 大括号都是成对出现的，缺一不可。[习惯，先写科再写代码]
6. 一个源文件中最多只能有一个public类。其它类的个数不限。
7. 如果源文件包含一个public类，则文件名必须按该类名命名!
8. 一个源文件中最多只能有一个public类。其它类的个数不限，也可以将main方法写在非public类中，然后指定运行非public类，这样入口方法就是非public的main方法

补充一些有关Java的专业术语：
- JDK（Java Development Kit）：编写Java程序的程序员使用的软件
- JRE（Java Runtime Environment）：运行Java程序的用户使用的软件
- Server JRE （Java SE Runtime Environment）：服务端使用的 Java 运行环境
- SDK（Software Development Kit）：软件开发工具包，在Java中用于描述1998年~2006年之间的JDK
- DAO（Data Access Object）：数据访问接口，数据访问，顾名思义就是与数据库打交道
- MVC（Model View Controller）：模型(model)－视图(view)－控制器(controller)的缩写，一种软件设计典范，用于组织代码用一种业务逻辑和数据显示分离的方法

## 2 第一个Java程序


创建文件名为`HelloWorld.java`(文件名需与类名一致)，代码如下：
```java
public class HelloWorld {
    public static void main(String[] args) {
        System.out.println("Hello World!");
    }
}
```
代码解释：
`public static void main(String[] args)`这是 Java 程序的入口地址，Java 虚拟机运行程序的时候首先找的就是 main 方法。跟 C 语言里面的 main() 函数的作用是一样的。只有有 main() 方法的 Java 程序才能够被 Java 虚拟机运行，可理解为规定的格式。

对于里面的参数及修饰符：
- public：表示的这个程序的访问权限，表示的是任何的场合可以被引用，这样 Java 虚拟机就可以找到 main() 方法,从而来运行 javac 程序。
- static： 表明方法是静态的，不依赖类的对象的，是属于类的，在类加载的时候 main() 方法也随着加载到内存中去。
- void main()：方法是不需要返回值的。
- main：约定俗成，规定的。
- String[] args：从控制台接收参数。

注：String args[] 与 String[] args 都可以执行，但推荐使用 String[] args，这样可以避免歧义和误读。

在终端运行该程序：
```bash
$ javac HelloWorld.java
$ java HelloWorld
Hello World!
```
执行命令解析：
以上我们使用了两个命令 javac 和 java。
- javac 后面跟着的是java文件的文件名，例如 HelloWorld.java。 该命令用于将 java 源文件编译为 class 字节码文件，如： `javac HelloWorld.java`。
- 运行javac命令后，如果成功编译没有错误的话，会出现一个 `HelloWorld.class` 的文件。
- java 后面跟着的是java文件中的类名,例如 HelloWorld 就是类名，如: `java HelloWorld`。

注意：java命令后面不要加.class。

