import java.util.List;

public class InsertQuery extends SQLQuery {
    private List<String> values;

    public InsertQuery(String tableName, List<String> values) {
        super(tableName);
        this.values = values;
    }

    @Override
    public String generateSQL() {
        String valuePart = String.join(", ", values);
        return "INSERT INTO " + tableName + " VALUES (" + valuePart + ");";
    }
}
