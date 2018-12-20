import { FoodType } from '../food-types/food-types.model';

export interface FoodRegistration {
  date: string;
  slot: number;
  eaten: FoodType[];
}
