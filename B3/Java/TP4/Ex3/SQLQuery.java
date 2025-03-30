// SQLQuery.java
public abstract class SQLQuery {
    protected String tableName;

    public SQLQuery(String tableName) {
        this.tableName = tableName;
    }

    public abstract String generateSQL();
}

