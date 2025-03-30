public class CreateTableQuery extends SQLQuery {

    public CreateTableQuery(String tableName) {
        super(tableName);
    }

    @Override
    public String generateSQL() {
        return "CREATE TABLE " + tableName + " (...);";
    }
}