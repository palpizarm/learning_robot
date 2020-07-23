using System;

namespace learning_robot
{
    public class Square
    {
        private int type { set; get; }
        private float cost { set; get; }
        
        public Square(int p_type, int p_cost)
        {
            type = p_type;
            cost = p_cost;
        }
    }

}