atachment_radias = 10;


atachment_height = 60;


skeawer_width = atachment_radias-3;




difference(){
  union(){
    cylinder(r=atachment_radias,h=atachment_height);
    translate([0,0,atachment_height*2])
    cube([atachment_radias*2,atachment_radias*5,atachment_height*2],center=true);
    }
    
    
    
  cylinder(r=skeawer_width , h=atachment_height-3);
}

