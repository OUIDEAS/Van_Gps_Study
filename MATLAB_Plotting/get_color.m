function [color, plotstatus] = get_color(soln_type, plotstatus)

    %% Var Init

    %% Get the things
    
    % color stuff here
    if soln_type == 'INS_RTKFIXED'
        
        color = plotstatus.INS_RTKFIXED.col; % []
        plotstatus.INS_RTKFIXED.stat = 1;
        
    elseif soln_type == 'INS_RTKFLOAT'
        
        color = plotstatus.INS_RTKFLOAT.col; % []
        plotstatus.INS_RTKFLOAT.stat = 1;
        
    elseif soln_type == 'NARROW_INT'
        
        color = plotstatus.NARROW_INT.col; % []
        plotstatus.NARROW_INT.stat = 1;
        
    elseif soln_type == 'PSRDIFF'
        
        color = plotstatus.PSRDIFF.col; % []
        plotstatus.PSRDIFF.stat = 1;
        
    elseif soln_type == 'PSRSP'
        
        color = plotstatus.PSRSP.col; % []
        plotstatus.PSRSP.stat = 1;
    
        
    elseif soln_type == 'INS_PSRSP'
        
        color = plotstatus.INS_PSRSP.col;
        plotstatus.INS_PSRSP.stat = 1;
        
    elseif soln_type == 'INS_PPP'
                
        color = plotstatus.INS_PPP.col;
        plotstatus.INS_PPP.stat = 1;
        
    elseif soln_type == 'INS_PPP_CONVERGING'
                
        color = plotstatus.INS_PPP_CONVERGING.col;
        plotstatus.INS_PPP_CONVERGING.stat = 1;
        
    elseif soln_type == 'PPP_CONVERGING'
        
        color = plotstatus.PPP_CONVERGING.col;
        plotstatus.PPP_CONVERGING.stat = 1;
        
    elseif soln_type == 'INS_PSRDIFF'
        
        color = plotstatus.INS_PSRDIFF.col;
        plotstatus.INS_PSRDIFF.stat = 1;
        
    elseif soln_type == 'NARROW_FLOAT'
        
        color = plotstatus.NARROW_FLOAT.col;
        plotstatus.NARROW_FLOAT.stat = 1;
        
    elseif soln_type == 'L1_FLOAT'
        
        color = plotstatus.L1_FLOAT.col;
        plotstatus.L1_FLOAT.stat = 1;
        
    end
    
end