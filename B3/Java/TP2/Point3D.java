public class Point3D extends Point {
    private float z ;

    public Point3D(float x , float y , float z){
        super(x , y);
        this.z = z;
        
        System.out.println(this.x);
    }
    public void volume()
    {
        System.out.println("Je suis une methode de Point3D");
    }
    public static void main(String[] args) {
        Point3D p  = new Point3D(1.0f, 2.0f, 3.0f);
        p.volume();

    }
}   
