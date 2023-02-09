public class HELLOWORLD {
    public static void main(String[] args) {
        //定义拥有的币种
        int[] money = {1, 5, 10, 20, 50, 100};
        //需要组成的金额
        int n = 10;
        //存储行的组合次数
        int[] li = new int[n + 1];
        //设定初始值
        li[0] = 1;
        //输出X轴值  （需要合成的金额）
        System.out.printf("%4d | ", 0);
        for (int i = 1; i < n + 1; i++) {
            System.out.printf("%4d", i);
        }

        //为了美观。。。。没有意义
        System.out.println();
        for (int i = 0; i < n + 2; i++) {
            System.out.printf("%4s", "——");
        }
        System.out.println();
        
        for (int m : money) {
            //输出Y轴坐标轴值 （拥有金额）
            System.out.printf("%4d | ", m);
            for (int i = 1; i <= n; i++) {
                if (i >= m) {
                    li[i] = li[i] + li[i - m];
                }
            }
            sout(li);
        }
    }

    //输出当前组合值
    private static void sout(int[] li) {
        for (int i = 1; i < li.length; i++) {
            System.out.printf("%4d", li[i]);
        }
        System.out.println();
    }
}