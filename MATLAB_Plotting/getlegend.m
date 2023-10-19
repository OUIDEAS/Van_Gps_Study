 function [h, legendLabels] = getlegend(plotstatus)
    
    %% VAR INIT
    
    legendLabels = {};
    plot_idx = 1;
    
    
    %% function
    
    if plotstatus.INS_RTKFIXED.stat
        h(plot_idx) = plot(NaN, NaN, 's', 'MarkerEdgeColor', 'k', 'MarkerFaceColor', [plotstatus.INS_RTKFIXED.col], 'MarkerSize', 20);
        legendLabels = [legendLabels, sprintf('\\color[rgb]{%f,%f,%f} INS RTKFIXED', plotstatus.INS_RTKFIXED.col(1), plotstatus.INS_RTKFIXED.col(2), plotstatus.INS_RTKFIXED.col(3))];
        plot_idx = plot_idx + 1;
        
    end
    
    if plotstatus.INS_RTKFLOAT.stat
        h(plot_idx) = plot(NaN, NaN, 's', 'MarkerEdgeColor', 'k', 'MarkerFaceColor', [plotstatus.INS_RTKFLOAT.col], 'MarkerSize', 20);
        legendLabels = [legendLabels, sprintf('\\color[rgb]{%f,%f,%f} INS RTKFLOAT', plotstatus.INS_RTKFLOAT.col(1), plotstatus.INS_RTKFLOAT.col(2), plotstatus.INS_RTKFLOAT.col(3))];
        plot_idx = plot_idx + 1;
    end
    
    if plotstatus.NARROW_INT.stat
        h(plot_idx) = plot(NaN, NaN, 's', 'MarkerEdgeColor', 'k', 'MarkerFaceColor', [plotstatus.NARROW_INT.col], 'MarkerSize', 20);
        legendLabels = [legendLabels, sprintf('\\color[rgb]{%f,%f,%f} NARROW INT', plotstatus.NARROW_INT.col(1), plotstatus.NARROW_INT.col(2), plotstatus.NARROW_INT.col(3))];
        plot_idx = plot_idx + 1;
    end
    
    if plotstatus.PSRDIFF.stat
        h(plot_idx) = plot(NaN, NaN, 's', 'MarkerEdgeColor', 'k', 'MarkerFaceColor', [plotstatus.PSRDIFF.col], 'MarkerSize', 20);
        legendLabels = [legendLabels, sprintf('\\color[rgb]{%f,%f,%f} PSRDIFF', plotstatus.PSRDIFF.col(1), plotstatus.PSRDIFF.col(2), plotstatus.PSRDIFF.col(3))];
        plot_idx = plot_idx + 1;
    end
    
    if plotstatus.PSRSP.stat
        h(plot_idx) = plot(NaN, NaN, 's', 'MarkerEdgeColor', 'k', 'MarkerFaceColor', [plotstatus.PSRSP.col], 'MarkerSize', 20);
        legendLabels = [legendLabels, sprintf('\\color[rgb]{%f,%f,%f} PSRSP', plotstatus.PSRSP.col(1), plotstatus.PSRSP.col(2), plotstatus.PSRSP.col(3))];
        plot_idx = plot_idx + 1;
    end
    
    if plotstatus.INS_PSRSP.stat
        h(plot_idx) = plot(NaN, NaN, 's', 'MarkerEdgeColor', 'k', 'MarkerFaceColor', [plotstatus.INS_PSRSP.col], 'MarkerSize', 20);
        legendLabels = [legendLabels, sprintf('\\color[rgb]{%f,%f,%f} INS PSRSP', plotstatus.INS_PSRSP.col(1), plotstatus.INS_PSRSP.col(2), plotstatus.INS_PSRSP.col(3))];
        plot_idx = plot_idx + 1;
    end
    
    if plotstatus.INS_PPP.stat
        h(plot_idx) = plot(NaN, NaN, 's', 'MarkerEdgeColor', 'k', 'MarkerFaceColor', [plotstatus.INS_PPP.col], 'MarkerSize', 20);
        legendLabels = [legendLabels, sprintf('\\color[rgb]{%f,%f,%f} INS PPP', plotstatus.INS_PPP.col(1), plotstatus.INS_PPP.col(2), plotstatus.INS_PPP.col(3))];
        plot_idx = plot_idx + 1;
    end
    
    if plotstatus.INS_PPP_CONVERGING.stat
        h(plot_idx) = plot(NaN, NaN, 's', 'MarkerEdgeColor', 'k', 'MarkerFaceColor', [plotstatus.INS_PPP_CONVERGING.col], 'MarkerSize', 20);
        legendLabels = [legendLabels, sprintf('\\color[rgb]{%f,%f,%f} INS PPP CONVERGING', plotstatus.INS_PPP_CONVERGING.col(1), plotstatus.INS_PPP_CONVERGING.col(2), plotstatus.INS_PPP_CONVERGING.col(3))];
        plot_idx = plot_idx + 1;
    end
    
    if plotstatus.PPP_CONVERGING.stat
        h(plot_idx) = plot(NaN, NaN, 's', 'MarkerEdgeColor', 'k', 'MarkerFaceColor', [plotstatus.PPP_CONVERGING.col], 'MarkerSize', 20);
        legendLabels = [legendLabels, sprintf('\\color[rgb]{%f,%f,%f} PPP CONVERGING', plotstatus.PPP_CONVERGING.col(1), plotstatus.PPP_CONVERGING.col(2), plotstatus.PPP_CONVERGING.col(3))];
        plot_idx = plot_idx + 1;
    end
    
    if plotstatus.INS_PSRDIFF.stat
        h(plot_idx) = plot(NaN, NaN, 's', 'MarkerEdgeColor', 'k', 'MarkerFaceColor', [plotstatus.INS_PSRDIFF.col], 'MarkerSize', 20);
        legendLabels = [legendLabels, sprintf('\\color[rgb]{%f,%f,%f} INS PSRDIFF', plotstatus.INS_PSRDIFF.col(1), plotstatus.INS_PSRDIFF.col(2), plotstatus.INS_PSRDIFF.col(3))];
        plot_idx = plot_idx + 1;
    end
    
    if plotstatus.NARROW_FLOAT.stat
        h(plot_idx) = plot(NaN, NaN, 's', 'MarkerEdgeColor', 'k', 'MarkerFaceColor', [plotstatus.NARROW_FLOAT.col], 'MarkerSize', 20);
        legendLabels = [legendLabels, sprintf('\\color[rgb]{%f,%f,%f} NARROW FLOAT', plotstatus.NARROW_FLOAT.col(1), plotstatus.NARROW_FLOAT.col(2), plotstatus.NARROW_FLOAT.col(3))];
        plot_idx = plot_idx + 1;
    end
    
    if plotstatus.L1_FLOAT.stat
        h(plot_idx) = plot(NaN, NaN, 's', 'MarkerEdgeColor', 'k', 'MarkerFaceColor', [plotstatus.L1_FLOAT.col], 'MarkerSize', 20);
        legendLabels = [legendLabels, sprintf('\\color[rgb]{%f,%f,%f} L1 FLOAT', plotstatus.L1_FLOAT.col(1), plotstatus.L1_FLOAT.col(2), plotstatus.L1_FLOAT.col(3))];
        plot_idx = plot_idx + 1;
    end
    
 end