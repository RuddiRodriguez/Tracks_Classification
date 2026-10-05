% TRACKFEATURESTEST: features describing different motion types.
% Original method credit: Jo Helmuth, Computational Biophysics Laboratory,
% ETHZ. Last change: May 23, 2007.
% Recovered from the Dropbox trackFeaturesTest.m preview; layout condensed.
% Original formulas and direction cases retained, including dy == 0 handling.

function features = trackFeaturesTest(x,y,windowWidth)
nPoints = length(x);
if(~(nPoints > windowWidth))
    warning('track too short to compute properties, I quit with empty output!');
    features = [];
    return;
end

squaredDisp = zeros(nPoints-windowWidth,1);
sumSquaredStep = zeros(nPoints-windowWidth,1);
straightness = zeros(nPoints-windowWidth,1);
Asym = zeros(nPoints-windowWidth,1);
bending = zeros(nPoints-windowWidth,1);
pointSkew = zeros(nPoints-windowWidth,1);
pointKurt = zeros(nPoints-windowWidth,1);
alpha = zeros(nPoints-1,1);
dx = diff(x);
dy = diff(y);
squaredSteps = dx.*dx + dy.*dy;

for j = 1:(nPoints-windowWidth)
    disp_x = x(j+windowWidth) - x(j);
    disp_y = y(j+windowWidth) - y(j);
    squaredDisp(j) = disp_x*disp_x + disp_y*disp_y;
    sumSquaredStep(j) = sum(squaredSteps(j:j+windowWidth-1));
    wx = x(j:j+windowWidth);
    wy = y(j:j+windowWidth);
    m_x = sum(wx)/(windowWidth+1);
    m_y = sum(wy)/(windowWidth+1);
    wx_mx = wx - m_x;
    wy_my = wy - m_y;
    R = [mean(wx_mx.^2) mean(wx_mx.*wy_my); ...
         mean(wx_mx.*wy_my) mean(wy_my.^2)];
    [EigVecR,EigR] = eig(R);
    Asym(j) = -log(1 - ((EigR(1)-EigR(4))^2) / ...
        (2*(EigR(1)+EigR(4))^2));
    if(EigR(1)>EigR(4))
        mainEVInd = 1;
    else
        mainEVInd = 2;
    end
    mainEV = EigVecR(:,mainEVInd);
    mainEV = mainEV/norm(mainEV);
    Proj = [wx_mx, wy_my]*mainEV;
    pointSkew(j) = abs(skewness(Proj));
    pointKurt(j) = kurtosis(Proj);
end

netDisp = sqrt(squaredDisp);
efficiency = (squaredDisp./windowWidth)./sumSquaredStep;
dx_eq_0 = find(dx==0);
dx_gt_0 = find(dx>0);
dx_lt_0 = find(dx<0);
dy_gteq_0 = find(dy>0);
dy_lt_0 = find(dy<0);
ind = intersect(dx_eq_0,dy_gteq_0);
alpha(ind) = 0.5*pi;
ind = intersect(dx_eq_0,dy_lt_0);
alpha(ind) = 1.5*pi;
ind = intersect(dx_gt_0,dy_gteq_0);
alpha(ind) = atan(dy(ind)./dx(ind));
ind = intersect(dx_lt_0,dy_gteq_0);
alpha(ind) = pi+atan(dy(ind)./dx(ind));
ind = intersect(dx_lt_0,dy_lt_0);
alpha(ind) = pi+atan(dy(ind)./dx(ind));
ind = intersect(dx_gt_0,dy_lt_0);
alpha(ind) = 2*pi+atan(dy(ind)./dx(ind));
beta = diff(alpha);
ind = find(beta < 0);
beta(ind) = beta(ind)+2*pi;
ind = find(beta > pi);
beta(ind) = beta(ind)-2*pi;
cosBeta = cos(beta);
sinBeta = sin(beta);
for j = 1:nPoints-windowWidth
    straightness(j) = sum(cosBeta(j:j+(windowWidth-2)));
    bending(j) = abs(sum(sinBeta(j:j+(windowWidth-2))));
end
straightness = straightness/(windowWidth-1);
bending = bending/(windowWidth-1);
features = [netDisp efficiency straightness Asym bending pointSkew pointKurt];
end
