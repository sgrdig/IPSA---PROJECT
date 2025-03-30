// Main.java
import java.util.Arrays;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        List<String> fields = Arrays.asList("name", "age");
        List<Condition> conditions = Arrays.asList(new Condition("age", ">", "30"), new Condition("city", "=", "'Paris'"));
        SelectQuery selectQuery = new SelectQuery("Users", fields, conditions);
        System.out.println(selectQuery.generateSQL());

        // Test Insert Query
        List<String> values = Arrays.asList("'John'", "28", "true");
        InsertQuery insertQuery = new InsertQuery("Users", values);
        System.out.println(insertQuery.generateSQL());

        // Test Create Table Query
        CreateTableQuery createTableQuery = new CreateTableQuery("Users");
        System.out.println(createTableQuery.generateSQL());

        // Test Drop Table Query
        DropTableQuery dropTableQuery = new DropTableQuery("Users");
        System.out.println(dropTableQuery.generateSQL());
    }
}
