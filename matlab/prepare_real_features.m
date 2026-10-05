function T = prepare_real_features(tracks_matlab, output_path)
% Feature preparation from the original main_script.m, with unused code removed.
% Keep its >4-position selection and full-track window length.
% D_DM remains a placeholder; it is not an experimental truth label.

names = {'Id','netDisp','efficiency','straightness','Asym', ...
    'bending','pointSkew','pointKurt','Classification','Track_length','Tracks'};
features = cell(length(tracks_matlab), length(names));
count = 0;
for i = 1:length(tracks_matlab)
    coordinates = tracks_matlab(i).tracksCoordAmpCG;
    x = coordinates(:,1:8:end);
    y = coordinates(:,2:8:end);
    available = find(~isnan(x));
    x = x(available)';
    y = y(available)';
    if length(x)>4
        count = count+1;
        features{count,1} = '';
        features(count,2:8) = num2cell(trackFeaturesTest(x,y,length(x)-1));
        features{count,9} = 'D_DM';
        features{count,10} = length(x);
        features{count,11} = [x y];
    end
end
% Remove unused preallocated rows before export; feature formulas stay unchanged.
T = cell2table(features(1:count,:), 'VariableNames', names);
writetable(T, output_path, 'Delimiter', ',', 'QuoteStrings', true);
end
