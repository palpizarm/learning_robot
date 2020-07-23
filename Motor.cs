using System;

namespace learning_robot
{
    class Motor
    {
        private int type { set; get; }
        private int power { set; get; }
        private int[] ground_type { set; get; }
        private float cost { set; get; }

        public Motor(int p_type, int p_power, int[] p_ground_type, float p_cost)
        {
            type = p_type;
            power = p_power;
            ground_type = p_ground_type;
            cost = p_cost;
        }
}
}