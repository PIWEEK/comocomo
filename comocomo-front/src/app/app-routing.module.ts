import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { LoginComponent } from './login/login.component';
import { DayComponent } from './day/day.component';
import { WeekComponent } from './week/week.component';
import { GatheringComponent } from './gathering/gathering.component';
import { BarnsComponent } from './barns/barns.component';

const routes: Routes = [
  { path: 'login', component: LoginComponent},
  { path: 'week', component: WeekComponent},
  { path: 'day', component: DayComponent},
  { path: 'day/:date/:slot', component: GatheringComponent},
  { path: 'barns', component: BarnsComponent},
  { path: '', redirectTo: '/login', pathMatch: 'full' },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
