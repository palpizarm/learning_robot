using System;
using System.IO;

namespace learning_robot
{
    class Grid
    {
        private Square[,] grid = new Square[util.GRD_LENGTH, util.GRD_LENGTH];

        public void createGrid(string p_path)
        {
            string[] grid_map = File.ReadAllLines(p_path);
            string[] values = new String[util.GRD_LENGTH];
            int type;
            for (int row = 0; row < util.GRD_LENGTH; row++)
            {
                values = grid_map[row].Split(',');
                for (int column = 0; column < util.GRD_LENGTH; column++) {
                    type = int.Parse(values[column]);
                    if (util.NORMAL_GROUND == type)
                        grid[row, column] = new Square(type, util.NORMAL_GRD_COST); 
                    else if (util.MODERATE_GROUND == type)
                        grid[row, column] = new Square(type, util.MODERATE_GRD_COST); 
                    else if (util.HARD_GROUND == type) 
                        grid[row, column] = new Square(type, util.HARD_GRD_COST); 
                    else if (util.LOCKED_GROUND == type) 
                        grid[row, column] = new Square(type, util.LOCKED_GRD_COST); 
                }
            }
        }
    }
}