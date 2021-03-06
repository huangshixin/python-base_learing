from  torchvision.models.resnet import  resnet101
import torch
import  torch.nn as nn



#定义BasicBlock
class BasicBlock(nn.Module):
    expansion = 1

    def __init__(self, inplanes, planes, stride=1, downsaple=None, groups=1,
                 base_width=64, dilation=1, norm_layer=None):
        super(BasicBlock, self).__init__()
        if norm_layer is None:
            norm_layer = nn.BatchNorm2d
        if groups !=1 or base_width != 64:
            raise ValueError('BasicBlock only supports groups=1 and base_width=64')
        if dilation > 1:
            raise NotImplementedError("Dilation > 1 not supported in BasicBlock")

        #下面定义BasicBlock中的各个层
        self.conv1 = con3x3(inplanes, planes, stride)
        self.bn1 = norm_layer(planes)
        self.relu = nn.ReLU(inplace=True) #inplace为True表示进行原地操作，一般默认为False，表示新建一个变量存储操作
        self.conv2 = con3x3(planes, planes)
        self.bn2 = norm_layer(planes)
        self.dowansample = downsaple
        self.stride = stride

    #定义前向传播函数将前面定义的各层连接起来
    def forward(self, x):
        identity = x #这是由于残差块需要保留原始输入

        out = self.conv1(x)
        out = self.bn1(out)
        out = self.relu(out)

        out = self.conv2(out)
        out = self.bn2(out)

        if self.dowansample is not None: #这是为了保证原始输入与卷积后的输出层叠加时维度相同
            identity = self.dowansample(x)

        out += identity
        out = self.relu(out)

        return out


#下面定义Bottleneck层（Resnet50以上用到的基础块）
class Bottleneck(nn.Module):
    expansion = 4 #Bottleneck层输出通道都是输入的4倍

    def __init__(self, inplanes, planes, stride=1, downnsaple=None, groups=1,
                 base_width=64, dilation=1, norm_layer=None):
        super(Bottleneck, self).__init__()
        if norm_layer is None:
            norm_layer = nn.BatchNorm2d
        width = int(planes * (base_width / 64.)) * groups
        #定义Bottleneck中各层
        self.conv1 = con1x1(inplanes, width)
        self.bn1 = norm_layer(width)
        self.conv2 = con3x3(width, width, stride, groups, dilation)
        self.bn2 = norm_layer(width)
        self.conv3 = con1x1(width, planes * self.expansion)
        self.bn3 = norm_layer(planes * self.expansion)
        self.relu = nn.ReLU(inplanes=True)
        self.downsaple = downnsaple
        self.stride = stride

    #定义Bottleneck的前向传播
    def forward(self, x):
        identity = x

        out = self.conv1(x)
        out = self.bn1(out)
        out = self.relu(out)

        out = self.conv2(out)
        out = self.bn2(out)
        out = self.relu(out)

        out = self.conv3(out)
        out = self.bn3(out)
        out = self.relu(out)

        if self.downsaple is not None:
            identity = self.downsaple(x)

        out += identity
        out = self.relu(out)

        return out


################################################################################################
#提供官方预训练模型的下载地址
model_urls = {
    'resnet18': 'https://download.pytorch.org/models/resnet18-5c106cde.pth',
    'resnet34': 'https://download.pytorch.org/models/resnet34-333f7ec4.pth',
    'resnet50': 'https://download.pytorch.org/models/resnet50-19c8e357.pth',
    'resnet101': 'https://download.pytorch.org/models/resnet101-5d3b4d8f.pth',
    'resnet152': 'https://download.pytorch.org/models/resnet152-b121ed2d.pth',
    'resnext50_32x4d': 'https://download.pytorch.org/models/resnext50_32x4d-7cdf4587.pth',
    'resnext101_32x8d': 'https://download.pytorch.org/models/resnext101_32x8d-8ba56ff5.pth',
    'wide_resnet50_2': 'https://download.pytorch.org/models/wide_resnet50_2-95faca4d.pth',
    'wide_resnet101_2': 'https://download.pytorch.org/models/wide_resnet101_2-32ee1156.pth',
}

#封装下3x3卷积层（卷积层的bias置为False是因为卷积层后面要加BN层，因此这里的bias不需要）
#Conv2d函数的具体参数说明可参见Pytorch官方手册https://pytorch-cn.readthedocs.io/zh/latest/package_references/torch-nn/#_1
def con3x3(in_planes, out_planes, stride=1, groups=1, dilation=1):
    return nn.Conv2d(in_planes, out_planes, kernel_size=3, stride=stride,
                     padding=dilation, groups=groups, bias=False, dilation=dilation)

#封装下1x1卷积层
def con1x1(in_planes, out_planes, stride=1):
    return nn.Conv2d(in_planes, out_planes, kenerl_size=1, stride=stride, bias=False)

#定义BasicBlock
class BasicBlock(nn.Module):
    expansion = 1

    def __init__(self, inplanes, planes, stride=1, downsaple=None, groups=1,
                 base_width=64, dilation=1, norm_layer=None):
        super(BasicBlock, self).__init__()
        if norm_layer is None:
            norm_layer = nn.BatchNorm2d
        if groups !=1 or base_width != 64:
            raise ValueError('BasicBlock only supports groups=1 and base_width=64')
        if dilation > 1:
            raise NotImplementedError("Dilation > 1 not supported in BasicBlock")

        #下面定义BasicBlock中的各个层
        self.conv1 = con3x3(inplanes, planes, stride)
        self.bn1 = norm_layer(planes)
        self.relu = nn.ReLU(inplace=True) #inplace为True表示进行原地操作，一般默认为False，表示新建一个变量存储操作
        self.conv2 = con3x3(planes, planes)
        self.bn2 = norm_layer(planes)
        self.dowansample = downsaple
        self.stride = stride

    #定义前向传播函数将前面定义的各层连接起来
    def forward(self, x):
        identity = x #这是由于残差块需要保留原始输入

        out = self.conv1(x)
        out = self.bn1(out)
        out = self.relu(out)

        out = self.conv2(out)
        out = self.bn2(out)

        if self.dowansample is not None: #这是为了保证原始输入与卷积后的输出层叠加时维度相同
            identity = self.dowansample(x)

        out += identity
        out = self.relu(out)

        return out

#下面定义Bottleneck层（Resnet50以上用到的基础块）
class Bottleneck(nn.Module):
    expansion = 4 #Bottleneck层输出通道都是输入的4倍

    def __init__(self, inplanes, planes, stride=1, downnsaple=None, groups=1,
                 base_width=64, dilation=1, norm_layer=None):
        super(Bottleneck, self).__init__()
        if norm_layer is None:
            norm_layer = nn.BatchNorm2d
        width = int(planes * (base_width / 64.)) * groups
        #定义Bottleneck中各层
        self.conv1 = con1x1(inplanes, width)
        self.bn1 = norm_layer(width)
        self.conv2 = con3x3(width, width, stride, groups, dilation)
        self.bn2 = norm_layer(width)
        self.conv3 = con1x1(width, planes * self.expansion)
        self.bn3 = norm_layer(planes * self.expansion)
        self.relu = nn.ReLU(inplanes=True)
        self.downsaple = downnsaple
        self.stride = stride

    #定义Bottleneck的前向传播
    def forward(self, x):
        identity = x

        out = self.conv1(x)
        out = self.bn1(out)
        out = self.relu(out)

        out = self.conv2(out)
        out = self.bn2(out)
        out = self.relu(out)

        out = self.conv3(out)
        out = self.bn3(out)
        out = self.relu(out)

        if self.downsaple is not None:
            identity = self.downsaple(x)

        out += identity
        out = self.relu(out)

        return out

#下面进入正题，定义ResNet类
class ResNet(nn.Module):
    def __init__(self, block, layer, num_classes=1000, zero_init_residual=False,
                 groups=1, width_per_group=64, replace_stride_with_dilation=None,
                 norm_layer=None):
        super(ResNet, self).__init__()
        if norm_layer is None:
            norm_layer = nn.BatchNorm2d
        self._norm_layer = norm_layer

        self.inplanes = 64
        self.dilation = 1
        if replace_stride_with_dilation is None:
            replace_stride_with_dilation = [False, False, False]
        if len(replace_stride_with_dilation) != 3:
            raise ValueError("replace_stride_with_dilation should be None "
                             "or a 3-element tuple, got {}".format(replace_stride_with_dilation))
        self.groups = groups
        self.base_width = width_per_group
        self.conv1 = nn.Conv2d(3, self.inplanes, kernel_size=7, stride=2, padding=3,
                               bias=False)
        self.bn1 = norm_layer(self.inplanes)
        self.relu = nn.ReLU(self.inplanes)
        self.maxpool = nn.MaxPool2d(kernel_size=3, stride=2, padding=1)
        self.layer1 = self._make_layer(block, 64, layer[0])
        self.layer2 = self._make_layer(block, 128, layer[1], stride=2,
                                       dilate=replace_stride_with_dilation[0])
        self.layer3 = self._make_layer(block, 256, layer[2], stride=2,
                                       dilate=replace_stride_with_dilation[1])
        self.layer4 = self._make_layer(block, 512, layer[3], stride=2,
                                       dilate=replace_stride_with_dilation[2])
        self.avgpool = nn.AdaptiveAvgPool2d((1,1))
        self.fc = nn.Linear(512 * block.expanion, num_classes)

        #定义初始化方式
        for m in self.modules():
            if isinstance(m, nn.Conv2d):
                nn.init.kaiming_nomal_(m.weight, mode='fan_out', nonlinearity='relu')
            elif isinstance(m, (nn.BatchNorm2d, nn.GroupNorm)):
                nn.init.constant_(m.weight, 1)
                nn.init.constant_(m.bias, 0)

        if zero_init_residual:
            for m in self.modules():
                if isinstance(m, Bottleneck):
                    nn.init.constant_(m.bn3.weight, 0)
                elif isinstance(m, BasicBlock):
                    nn.init.constant_(m.bn2.weight, 0)
    def _make_layer(self, block, planes, blocks, stride=1, dilate=False):
        norm_layer = self._norm_layer
        downsaple = None
        previous_dilation = self.dilation
        if dilate:
            self.dilation *= stride
            stride = 1
        if stride != 1 or self.inplanes != planes * block.expanion:
            downsaple = nn.Sequential(
                con1x1(self.inplanes, planes * block.expanion, stride),
                norm_layer(planes * block.expanion),
            )

        layers = []
        layers.append(block(self.inplanes, planes, stride, downsaple, self.groups,
                            self.base_width, previous_dilation, norm_layer))
        self.inplanes = planes * block.expanion
        for _ in range(1, block):
            layers.append(block(self.inplanes, planes, groups=self.groups,
                                base_width=self.base_width, dilate=self.dilation,
                                norm_layer=norm_layer))

        return  nn.Sequential(*layers)

    def _forward_impl(self, x):
        x = self.conv1(x)
        x = self.bn1(x)
        x = self.relu(x)
        x = self.maxpool(x)

        x = self.layer1(x)
        x = self.layer2(x)
        x = self.layer3(x)
        x = self.layer4(x)

        x = self.avgpool(x)
        x = torch.flatten(x, 1)
        x = self.fc(x)

        return x

    def forward(self, x):
        return self._forward_impl(x)

    def _resnet(arch, block, layers, pretrained, progress, **kwargs):
        model = ResNet(block, layers, **kwargs)
        if pretrained:
            state_dict = load_state_dict_from_url(model_urls[arch],
                                                  progress=progress)
            model.load_state_dict(state_dict)
        return model

    def resnet34(pretrained=False, progress=True, **kwargs):
        return _resnet('resnet34', BasicBlock, [3, 4, 6, 3], pretrained, progress,
                       **kwargs)

    def resnet101(pretrained=False, progress=True, **kwargs):
        return _resnet('resnet101', Bottleneck, [3, 4, 23, 3], pretrained, progress,
                       **kwargs)
