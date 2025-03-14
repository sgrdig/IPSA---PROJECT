

public class Point {
    private float x;
    private float y;

    public Point(float xCo, float yCo) {
        this.x = xCo;
        this.y = yCo;
    }

    public Point(Point other) {
        this.x = other.x;
        this.y = other.y;
    }

    public Point() {
        this.x = 1;
        this.y = 2;
    }

    public void affiche() {
        System.out.println("x: " + this.x);
        System.out.println("y: " + this.y);
    }

    public void deplacer(float dx, float dy) {
        this.x += dx;
        this.y += dy;
    }

    public void setX(float xCo) {
        this.x = xCo;
    }

    public float getY() {
        return this.y;
    }

    
    public Boolean equals(Point p){
        if (p.x == this.x && p.y == this.y){
            return true ;
        }   
        return false ; 
        

        
        
    }

    public static void main(String[] args) {
        Point p1 = new Point(2.01f, 3.03f);
        p1.affiche();

        Point p2 = new Point(2.01f, 3.03f);
        p2.affiche();
        
        Boolean verif = p1.equals(p2);
        System.out.println(verif);



        System.out.println(p1 == p2);

        Point p3 = new Point(p1);
        p3.affiche();

        p1.deplacer(1.0f, 1.0f);
        p1.affiche();

        p1.setX(5.0f);
        p1.affiche();
        System.out.println("y-coordinate of p1: " + p1.getY());
    }
}
