function cyberCSV = cyberCSVImport(filename)
%IMPORTFILE Import data from a text file
%  CYBER2BESTPOSE1697482416 = IMPORTFILE(FILENAME) reads data from text
%  file FILENAME for the default selection.  Returns the data as a table.
%
%  CYBER2BESTPOSE1697482416 = IMPORTFILE(FILE, DATALINES) reads data for
%  the specified row interval(s) of text file FILENAME. Specify
%  DATALINES as a positive scalar integer or a N-by-2 array of positive
%  scalar integers for dis-contiguous row intervals.
%
%  Example:
%  cyber2bestpose1697482416 = importfile("/media/autobuntu/chonk/chonk/git_repos/cyber2csv/cyber2_best_pose_1697482416.0264118.csv", [2, Inf]);
%
%  See also READTABLE.
%
% Auto-generated by MATLAB on 16-Oct-2023 15:12:46

%% Input handling

% If dataLines is not specified, define defaults
if nargin < 2
    dataLines = [2, Inf];
end

%% Set up the Import Options and import the data
opts = delimitedTextImportOptions("NumVariables", 18);

% Specify range and delimiter
opts.DataLines = dataLines;
opts.Delimiter = ",";

% Specify column names and types
opts.VariableNames = ["latitude", "longitude", "latitudeStdDev", "longitudeStdDev", "heightStdDev", "galileoBeidouUsedMask", "solutionAge", "extendedSolutionStatus", "solStatus", "heightMsl", "baseStationId", "numSatsTracked", "numSatsInSolution", "solType", "datumId", "numSatsL1", "differentialAge", "timestamp"];
opts.VariableTypes = ["double", "double", "double", "double", "double", "double", "double", "double", "categorical", "double", "double", "double", "double", "categorical", "double", "double", "double", "double"];

% Specify file level properties
opts.ExtraColumnsRule = "ignore";
opts.EmptyLineRule = "read";

% Specify variable properties
opts = setvaropts(opts, ["solStatus", "solType"], "EmptyFieldRule", "auto");
opts = setvaropts(opts, ["baseStationId", "datumId"], "TrimNonNumeric", true);
opts = setvaropts(opts, ["baseStationId", "datumId"], "ThousandsSeparator", ",");

% Import the data
cyberCSV = readtable(filename, opts);

end