%% Multi_Log_Plotter
% scans a txt file that contains the output from several logs and plots the
% following:
% inspvax, bestpos, ppppos, rtkpos std vs time (can choose which to plot)
% bestpos solution type vs time, displayed as a background colored area
% lines showing at which point something changed

clear all
close all
clc


%% OPTIONS

% Opacity of the areas - should be less than one
patchfacealpha                      = .25;


%% VAR INIT

% Load File
file_to_load = "/media/autobuntu/chonk/chonk/git_repos/cyber2csv/cyber2_best_pose_1697482416.0264118.csv";
cyberCSV = cyberCSVImport(file_to_load);

% Initializes the timestamp
bestpos_ts                          = cyberCSV.timestamp;

% Converts the timestamp to local time for easier diagnostics
bestpos_ts                          = bestpos_ts - bestpos_ts(1);

% Initializes the solution type
bp_pos_type                         = cyberCSV.solType;

% Initializes the solution types used on the plot.
plotstatus.INS_RTKFIXED.stat        = 0;
plotstatus.INS_RTKFLOAT.stat        = 0;
plotstatus.NARROW_INT.stat          = 0;
plotstatus.PSRDIFF.stat             = 0;
plotstatus.PSRSP.stat               = 0;
plotstatus.INS_PSRSP.stat           = 0;
plotstatus.INS_PPP.stat             = 0;
plotstatus.INS_PPP_CONVERGING.stat  = 0;
plotstatus.PPP_CONVERGING.stat      = 0;
plotstatus.INS_PSRDIFF.stat         = 0;
plotstatus.NARROW_FLOAT.stat        = 0;
plotstatus.L1_FLOAT.stat            = 0;

% Initializes the color for each solution type.
plotstatus.INS_RTKFIXED.col         = [0.9160    0.6074    0.6476];
plotstatus.INS_RTKFLOAT.col         = [0.0012    0.1917    0.6790];
plotstatus.NARROW_INT.col           = [0.4624    0.7384    0.6358];
plotstatus.PSRDIFF.col              = [0.4243    0.2428    0.9452];
plotstatus.PSRSP.col                = [0.4609    0.9174    0.2089];
plotstatus.INS_PSRSP.col            = [0.7702    0.2691    0.7093];
plotstatus.INS_PPP.col              = [0.3225    0.7655    0.2362];
plotstatus.INS_PPP_CONVERGING.col   = [0.7847    0.1887    0.1194];
plotstatus.PPP_CONVERGING.col       = [0.4714    0.2875    0.6073];
plotstatus.INS_PSRDIFF.col          = [0.0358    0.0911    0.4501];
plotstatus.NARROW_FLOAT.col         = [0.9759    0.5762    0.4587];
plotstatus.L1_FLOAT.col             = [0.7218    0.1834    0.1619];

            
%% Standard Deviation

% Calculates the standard deviation magnitude
latlonstdmag = sqrt((cyberCSV.latitudeStdDev).^2 + (cyberCSV.longitudeStdDev));


%% BestPos Solution Type Breaks

% Converts the solution type into a double - this allows for more easily
% finding the changes between solution types.
bp_numeric_values       = double(cyberCSV.solType);

% Determines the indexes of the changes. Index is the value *before* the
% change.
bp_category_changes     = find(diff(bp_numeric_values) ~= 0);


if isempty(bp_category_changes)
    
    bp_category_changes = [length(bp_pos_type)];
    
end


%% Plotting Logic

% Setting the bounds for the solution type hatches
area_y_max = max(latlonstdmag) + 1;
patch_y = [0, 0, area_y_max, area_y_max];

% Initilizes the figure
stdcompfig = figure('DefaultAxesFontSize', 24);
hold on

% Plotting the magnitude of the standard deviation over time
scatter(bestpos_ts, latlonstdmag, 'r', 'Filled')

% DEBUG: Sets up an array for the hatches to see where the start/end
temp_x_array = []; % unused - for diag only

% Goes through each solution type change to plot colored areas
for change_idx = 1:length(bp_category_changes)

    % Starting condition
    if change_idx == 1
        
        [color, plotstatus] = get_color(bp_pos_type(bp_category_changes(change_idx)-1), plotstatus);
        
        patch_x = [bestpos_ts(1), bestpos_ts(bp_category_changes(change_idx)), bestpos_ts(bp_category_changes(change_idx)), bestpos_ts(1)];
        
        patch(patch_x, patch_y, color, 'FaceAlpha', patchfacealpha);
        temp_x_array = [temp_x_array; patch_x];
     
    % Ending condition
    elseif change_idx == length(bp_category_changes)

        % Last item in bp_category_changes - 2nd to last patch
        [color, plotstatus] = get_color(bp_pos_type(bp_category_changes(change_idx)-1), plotstatus);
        
        patch_x = [bestpos_ts(bp_category_changes(change_idx-1)), bestpos_ts(bp_category_changes(change_idx)-1), bestpos_ts(bp_category_changes(change_idx)-1), bestpos_ts(bp_category_changes(change_idx-1))];
        patch(patch_x, patch_y, color, 'FaceAlpha', patchfacealpha);
        temp_x_array = [temp_x_array; patch_x];

        % Last patch
        [color, plotstatus] = get_color(bp_pos_type(bp_category_changes(change_idx)+1), plotstatus);
        
        patch_x = [bestpos_ts(bp_category_changes(change_idx)-1), bestpos_ts(end), bestpos_ts(end), bestpos_ts(bp_category_changes(change_idx)-1)];
        patch(patch_x, patch_y, color, 'FaceAlpha', patchfacealpha);
        temp_x_array = [temp_x_array; patch_x];
    
    % All other conditions
    else
        
        [color, plotstatus] = get_color(bp_pos_type(bp_category_changes(change_idx)-1), plotstatus);
        
        patch_x = [bestpos_ts(bp_category_changes(change_idx-1)), bestpos_ts(bp_category_changes(change_idx)), bestpos_ts(bp_category_changes(change_idx)), bestpos_ts(bp_category_changes(change_idx-1))];
        patch(patch_x, patch_y, color, 'FaceAlpha', patchfacealpha);
        temp_x_array = [temp_x_array; patch_x];
        
    end
     
end


[h, legendLabels] = getlegend(plotstatus);

l = legend(h, legendLabels,...
    'FontSize', 24,...
    'FontWeight',...
    'bold',...
    'LineWidth', 4);
l.Interpreter = 'tex';

xlabel('time (s)')
ylabel('std (m)')
xlim([bestpos_ts(1), bestpos_ts(end)])

