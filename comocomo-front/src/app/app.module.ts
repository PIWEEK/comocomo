import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { ReactiveFormsModule } from '@angular/forms';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { SvgSpriteComponent } from './shared/svg-sprite/svg-sprite.component';
import { LoginComponent } from './login/login.component';
import { WeekComponent } from './week/week.component';
import { DayComponent } from './day/day.component';
import { BarnsComponent } from './barns/barns.component';
import { GatheringComponent } from './gathering/gathering.component';
import { MenuBarComponentComponent } from './shared/menu-bar-component/menu-bar-component.component';
import { NavBarComponentComponent } from './shared/nav-bar-component/nav-bar-component.component';

@NgModule({
  declarations: [
    AppComponent,
    SvgSpriteComponent,
    LoginComponent,
    WeekComponent,
    DayComponent,
    BarnsComponent,
    GatheringComponent,
    MenuBarComponentComponent,
    NavBarComponentComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    ReactiveFormsModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
