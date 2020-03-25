/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package ml_wine;
import csvreader.CSVReader;
/**
 *
 * @author Camilo
 */
public class ML_Wine {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        CSVReader reader = new CSVReader("winequality.csv");
    }
    
}
