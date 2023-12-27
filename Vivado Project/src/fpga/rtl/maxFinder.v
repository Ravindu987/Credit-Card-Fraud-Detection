module maxFinder #(parameter numInput=10,parameter inputWidth=16)(
input           i_clk,
input [(numInput*inputWidth)-1:0]   i_data,
input           i_valid,
output reg [31:0]o_data,
output  reg     o_data_valid
);

reg [inputWidth-1:0] maxValue;
reg [(numInput*inputWidth)-1:0] inDataBuffer;
integer counter;

always @(posedge i_clk)
begin
    o_data_valid <= 1'b0;
    if(i_valid)
    begin
        maxValue <= i_data[inputWidth-1:0];
        counter <= 1;
        inDataBuffer <= i_data;
        o_data <= (i_data[inputWidth-1:0] > 12'b100000000000) ? 1 : 0;
        o_data_valid <= 1'b1;
    end
end

endmodule