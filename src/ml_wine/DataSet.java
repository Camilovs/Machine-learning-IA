/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package ml_wine;

/**
 *
 * @author Camilo
 */
public class DataSet {
    
    double[][] dataSet;
    
    public DataSet(int filas, int columnas){
        dataSet = new double[filas][columnas];
    }
    
    public void addData(int fila, int columna, double data){
        dataSet[fila][columna] = data;
    }

    public double[][] getDataSet() {
        return dataSet;
    }

    public void setDataSet(double[][] dataSet) {
        this.dataSet = dataSet;
    }
    
    public void printDataSet(){
        for (int i = 0; i < dataSet.length; i++) {
            for (int j = 0; j <dataSet[i].length; j++) {
                System.out.print(dataSet[i][j]+"|");
            }
            System.out.println("");
        }
    }
    
}
