import java.io.*;
import java.net.*;
 
public class SimpleClient {
    public static void main(String[] args) {
        String serverAddress = "localhost"; // Server IP or hostname
        int port = 80020; // Server port
 
        try (Socket socket = new Socket(serverAddress, port);
             PrintWriter out = new PrintWriter(socket.getOutputStream(), true);
             BufferedReader in = new BufferedReader(new InputStreamReader(socket.getInputStream()))) {
 
            // Send a message to the server
            String message = "Hello, Server!";
            out.println(message);
            System.out.println("Sent to server: " + message);
 
            // Read the server response
            String response = in.readLine();
            System.out.println("Received from server: " + response);
 
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
 