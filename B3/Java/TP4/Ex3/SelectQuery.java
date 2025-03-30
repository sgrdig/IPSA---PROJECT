import java.util.List;

public class SelectQuery extends SQLQuery {
    private List<String> fields;
    private List<Condition> conditions;

    public SelectQuery(String tableName, List<String> fields, List<Condition> conditions) {
        super(tableName);
        this.fields = fields;
        this.conditions = conditions;
    }
    

    @Override
    public String generateSQL() {
        StringBuffer sql = new StringBuffer("SELECT ");
        
        for (int i = 0; i < fields.size(); i++) {

            sql.append(fields.get(i));
            if (i < fields.size() - 1) {
                sql.append(", ");
            }
        }
        
        sql.append(" FROM ");
        sql.append(tableName);
        sql.append(" WHERE ");
        for (Object elem : conditions) {
            sql.append(elem.toString());
            if (elem == conditions.get(conditions.size() - 1)) {
                break;
            }
            sql.append(" AND ");
        }
        sql.append(";");

    return sql.toString();
    }


    public static void main(String[] args) {
        List<String> fields = List.of("name", "age");
        List<Condition> conditions = List.of(new Condition("age", ">", "30"), new Condition("city", "=", "'Paris'"));
        SelectQuery selectQuery = new SelectQuery("Users", fields, conditions);
        System.out.println(selectQuery.generateSQL());
    }
        



}
