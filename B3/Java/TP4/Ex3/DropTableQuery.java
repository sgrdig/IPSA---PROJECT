public class DropTableQuery extends SQLQuery {

    public DropTableQuery(String tableName) {
        super(tableName);
    }

    @Override
    public String generateSQL() {
        return "DROP TABLE " + tableName + ";";
    }
}
