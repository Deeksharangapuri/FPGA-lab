
module assgn1(
    input  wire clk,
input  wire A,
input  wire B,
input  wire C,
input  wire D,
    output reg a,//1-bit variable register // a, b, c, d, e, f, g are the final outputs.
    output reg b,
    output reg c,
    output reg d,
    output reg e,
    output reg f,
    output reg g,
    output reg N,
    output reg W,
    output reg X,
    output reg Y,
    output reg Z,
    

);
  initial 
  begin
    W=A;
  X=B;
  Y=C;
  Z=D;
       
       
end


 always @(posedge clk) begin
 N<=1;
 end

endmodule
